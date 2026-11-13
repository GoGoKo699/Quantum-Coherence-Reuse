#!/usr/bin/env python3
"""Check reader navigation and the common learning-map structure.

These source checks do not validate mathematical truth, citation priority,
learning effectiveness, or the actual hosted renderer.  No network is used.
"""
from __future__ import annotations

import argparse
import hashlib
import html
import json
import re
import unicodedata
from pathlib import Path
from urllib.parse import unquote, urlsplit


FIELDS = (
    "Central question",
    "Understanding target",
    "Dependencies and story role",
    "Conceptual connection",
    "Source pointers",
)
PRIVATE_PROSE_PATTERNS = (
    r"\bgame[_ -]checkpoint\b",
    r"\bexploration[_ -]deadline\b",
    r"\b(?:coaching guide|personal coaching|learner progress)\b",
    r"\b(?:retry challenge|remediation rounds|failed challenges)\b",
    r"\b(?:acceptance probability|target journal|journal targeting)\b",
    r"\bprojects/[^\s/]+/handoffs/",
)
PRIVATE_NAME_PATTERNS = (
    r"(?:^|/)(?:COACHING|learner[_-]progress|game[_-]checkpoint)(?:\.|/|$)",
    r"(?:^|/)(?:handoffs|personal[_-]coaching)(?:/|$)",
)


def without_fences(source: str) -> str:
    """Preserve line numbers while removing fenced code, including math fences."""
    result = []
    fence = None
    for line in source.splitlines(keepends=True):
        found = re.match(r"^ {0,3}(`{3,}|~{3,})", line)
        if fence is None and found:
            fence = (found.group(1)[0], len(found.group(1)))
            result.append("\n" if line.endswith("\n") else "")
        elif fence is not None:
            if found and found.group(1)[0] == fence[0] and len(found.group(1)) >= fence[1]:
                fence = None
            result.append("\n" if line.endswith("\n") else "")
        else:
            result.append(line)
    return "".join(result)


def prose(source: str) -> str:
    text = without_fences(source)
    text = re.sub(r"<!--.*?-->", "", text, flags=re.S)
    return re.sub(r"(`+)([^`\n]*?)\1", "", text)


def without_math(text: str) -> str:
    """Math brackets must not be mistaken for Markdown reference links."""
    blank = lambda found: "".join("\n" if c == "\n" else " " for c in found.group())
    text = re.sub(r"(?<!\\)\$\$[\s\S]*?(?<!\\)\$\$", blank, text)
    text = re.sub(r"(?<![\\$])\$(?!\$)(?:\\.|[^$\n])+?(?<!\\)\$(?!\$)", blank, text)
    text = re.sub(r"\\\[[\s\S]*?\\\]", blank, text)
    return re.sub(r"\\\([^\n]*?\\\)", blank, text)


def heading_slugs(source: str) -> set[str]:
    text = without_fences(source)
    headings = []
    lines = text.splitlines()
    for i, line in enumerate(lines):
        found = re.match(r"^ {0,3}#{1,6}\s+(.+?)\s*#*\s*$", line)
        if found:
            headings.append(found.group(1))
        elif i and re.match(r"^ {0,3}(?:=+|-+)\s*$", line) and lines[i-1].strip():
            headings.append(lines[i-1].strip())
    used = set()
    for heading in headings:
        heading = re.sub(r"!?\[([^\]]*)\]\([^)]*\)", r"\1", heading)
        heading = re.sub(r"<[^>]*>", "", heading)
        heading = html.unescape(heading).lower()
        # This covers the plain-language headings used by this repository.
        # Actual hosted IDs/rendering remain an independent review obligation.
        base = "".join(c for c in heading if c in " _-" or unicodedata.category(c)[0] in "LN")
        base = base.replace(" ", "-")
        candidate, suffix = base, 0
        while candidate in used:
            suffix += 1
            candidate = f"{base}-{suffix}"
        used.add(candidate)
    used.update(re.findall(r"<(?:a|[a-z][a-z0-9]*)\b[^>]*\b(?:id|name)=[\"']([^\"']+)[\"']", text, re.I))
    return used


def destination(raw: str) -> str:
    raw = raw.strip()
    if raw.startswith("<"):
        end = raw.find(">")
        return raw[1:end] if end >= 0 else raw
    # A whitespace-separated optional Markdown title is not part of the URL.
    return re.split(r"\s+[\"']", raw, maxsplit=1)[0].strip()


def markdown_links(source: str):
    """Read inline, explicit/collapsed reference, and HTML links outside code."""
    text = without_math(prose(source))
    definitions = {}
    for found in re.finditer(r"^ {0,3}\[([^\]\n]+)\]:\s*(<[^>]+>|\S+)", text, re.M):
        definitions[found.group(1).casefold()] = destination(found.group(2))
    # Scan balanced URL parentheses rather than stopping at the first ')'.
    position = 0
    while True:
        start = text.find("](", position)
        if start < 0:
            break
        cursor, depth = start+2, 1
        while cursor < len(text) and depth:
            if text[cursor] == "\\":
                cursor += 2
                continue
            depth += (text[cursor] == "(") - (text[cursor] == ")")
            cursor += 1
        if depth:
            yield {"target": "", "line": text[:start].count("\n")+1,
                   "malformed": "unclosed inline link destination"}
            break
        yield {"target": destination(text[start+2:cursor-1]),
               "line": text[:start].count("\n")+1}
        position = cursor
    reference_spans = []
    for found in re.finditer(r"!?\[([^\]\n]+)\]\[([^\]\n]*)\]", text):
        reference_spans.append(found.span())
        key = (found.group(2) or found.group(1)).casefold()
        if key in definitions:
            yield {"target": definitions[key], "line": text[:found.start()].count("\n")+1}
        else:
            yield {"target": "", "line": text[:found.start()].count("\n")+1,
                   "malformed": f"undefined link reference {key!r}"}
    for found in re.finditer(r"\b(?:href|src)=[\"']([^\"']+)[\"']", text, re.I):
        yield {"target": found.group(1), "line": text[:found.start()].count("\n")+1}
    # Shortcut references are relevant only when a definition exists.
    for found in re.finditer(r"(?<!!)\[([^\]\n]+)\](?![\[(])", text):
        if any(start <= found.start() < end for start,end in reference_spans):
            continue
        key = found.group(1).casefold()
        if key in definitions and not re.match(r"\s*:", text[found.end():]):
            yield {"target": definitions[key], "line": text[:found.start()].count("\n")+1}


def math_table_inventory(source: str) -> dict:
    text = without_fences(source)
    displays = len(re.findall(r"(?<!\\)\$\$[\s\S]*?(?<!\\)\$\$", text))
    inline = len(re.findall(r"(?<![\\$])\$(?!\$)(?:\\.|[^$\n])+?(?<!\\)\$(?!\$)", text))
    math_fences = len(re.findall(r"^ {0,3}(?:`{3,}|~{3,})math\s*$", source, re.M))
    lines = text.splitlines()
    plain_lines = without_math(text).splitlines()
    table_indices = set()
    for index,line in enumerate(plain_lines):
        cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
        separator = ("|" in line and cells and all(re.fullmatch(r":?-{3,}:?",cell) for cell in cells))
        if separator and index and "|" in plain_lines[index-1]:
            table_indices.update([index-1,index])
            following = index+1
            while following < len(plain_lines) and "|" in plain_lines[following]:
                table_indices.add(following)
                following += 1
    table_rows = [lines[index] for index in sorted(table_indices)]
    columns = [max(0, len(re.findall(r"(?<!\\)\|", row))-1) for row in table_rows]
    return {"display_dollar_pairs": displays, "inline_dollar_pairs": inline,
            "math_fences": math_fences, "table_rows": len(table_rows),
            "maximum_table_columns": max(columns, default=0),
            "maximum_table_source_line_length": max(map(len, table_rows), default=0),
            "layout_review_priority": bool(max(columns, default=0) >= 4 or
                                         any("$" in row or len(row)>180 for row in table_rows))}


def milestone_checks(path: Path, errors: list[str]) -> dict:
    if not path.is_file():
        errors.append("Missing learning/MILESTONES.md")
        return {}
    text = without_fences(path.read_text())
    matches = list(re.finditer(r"^###\s+(M\d{2})\b[^\n]*$", text, re.M))
    ids = [match.group(1) for match in matches]
    expected = [f"M{i:02}" for i in range(1,31)]
    if ids != expected:
        errors.append(f"Milestone heading IDs must appear exactly once in order M01…M30; found {ids}")
    phases = list(re.finditer(r"^##\s+Phase\s+(?:[12]|I{1,2})\b[^\n]*$", text, re.M))
    if len(phases) != 2:
        errors.append(f"Expected exactly two Phase headings; found {len(phases)}")
    if len(phases) == 2:
        if not re.search(r"background|preliminar|foundation", phases[0].group(), re.I):
            errors.append("First phase must identify background/preliminaries")
        if not re.search(r"narrative|innovation", phases[1].group(), re.I):
            errors.append("Second phase must identify narrative/innovation")
    phase_counts = {phase.group().lstrip("# "):0 for phase in phases}
    records = []
    field_pattern = re.compile(r"^\*\*("+"|".join(map(re.escape,FIELDS))+r"):?\*\*:?\s*(.*)$", re.M)
    for index, match in enumerate(matches):
        mid = match.group(1)
        end = matches[index+1].start() if index+1 < len(matches) else len(text)
        intervening_phases = [phase.start() for phase in phases if match.end() < phase.start() < end]
        if intervening_phases:
            end = min(intervening_phases)
        body = text[match.end():end]
        field_matches = list(field_pattern.finditer(body))
        fields = {}
        for j, field in enumerate(field_matches):
            finish = field_matches[j+1].start() if j+1 < len(field_matches) else len(body)
            value = (field.group(2)+body[field.end():finish]).strip()
            if field.group(1) in fields:
                errors.append(f"{mid}: duplicate {field.group(1)} field")
            fields[field.group(1)] = value
        for name in FIELDS:
            if not fields.get(name):
                errors.append(f"{mid}: missing or empty {name}")
        dependency_field = fields.get("Dependencies and story role", "")
        # The explicit dependency span avoids treating a forward story pointer
        # as a prerequisite.  A plain ID list also remains supported.
        dependency_span = re.split(r"\bStory role\s*:", dependency_field, maxsplit=1, flags=re.I)[0]
        dependencies = re.findall(r"\bM\d{2}\b", dependency_span)
        if not dependencies and not re.search(r"\bnone\b",dependency_span,re.I):
            errors.append(f"{mid}: prerequisite declaration must list IDs or say none")
        if len(dependencies) != len(set(dependencies)):
            errors.append(f"{mid}: repeated dependency IDs")
        for dependency in dependencies:
            if dependency not in expected or int(dependency[1:]) >= int(mid[1:]):
                errors.append(f"{mid}: prerequisite {dependency} is not an earlier milestone")
        enclosing = [phase for phase in phases if phase.start() < match.start()]
        phase = enclosing[-1].group().lstrip("# ") if enclosing else None
        if phase is None:
            errors.append(f"{mid}: no enclosing phase")
        else:
            phase_counts[phase] += 1
        records.append({"id":mid,"phase":phase,"dependencies":dependencies,
                        "fields":list(fields)})
    for phase,count in phase_counts.items():
        if count == 0:
            errors.append(f"Phase has no milestones: {phase}")
    return {"count":len(ids),"phase_counts":phase_counts,"records":records,
            "scope":"Field presence and dependency order only; conceptual depth and phase synthesis require reading."}


def run_checks(root: Path, extra_prose=(), extra_names=()) -> dict:
    errors = []
    markdown = sorted(path for path in root.rglob("*.md") if ".git" not in path.parts)
    readers = markdown+[root/"llms.txt"]
    readers = [path for path in readers if path.is_file()]
    required = ["README.md","llms.txt","science/README.md","science/model.md",
                "science/converse.md","science/construction.md","science/sequential_reuse.md",
                "references/RELATED_WORK.md","references/references.bib","verification/README.md"]
    for name in required:
        if not (root/name).is_file():
            errors.append(f"Missing reader destination {name}")
    all_files = [path for path in root.rglob("*") if path.is_file() and ".git" not in path.parts]
    for path in all_files:
        relative = path.relative_to(root).as_posix()
        if any(re.search(pattern,relative,re.I) for pattern in (*PRIVATE_NAME_PATTERNS,*extra_names)):
            errors.append(f"Private-process filename in reader tree: {relative}")
    slugs = {path.resolve():heading_slugs(path.read_text()) for path in readers}
    links_checked = 0
    inventory = []
    for path in readers:
        source = path.read_text()
        relative = path.relative_to(root).as_posix()
        clean = prose(source)
        for pattern in (*PRIVATE_PROSE_PATTERNS,*extra_prose):
            found = re.search(pattern,clean,re.I)
            if found:
                errors.append(f"{relative}: private workflow/editorial prose marker {found.group()!r}")
        for pattern in (*PRIVATE_PROSE_PATTERNS,*extra_prose):
            found = re.search(pattern,source,re.I)
            if found and not re.search(pattern,clean,re.I):
                errors.append(f"{relative}: private metadata marker inside code/markup {found.group()!r}")
        for link in markdown_links(source):
            if link.get("malformed"):
                errors.append(f"{relative}:{link['line']}: {link['malformed']}")
                continue
            target = html.unescape(link["target"])
            target = re.sub(r"\\([\\`*_{}\[\]()#+.!<>-])",r"\1",target)
            parsed = urlsplit(target)
            if parsed.scheme or parsed.netloc:
                continue
            links_checked += 1
            decoded = unquote(parsed.path).replace("\\ "," ")
            resolved = (path.parent/decoded).resolve() if decoded else path.resolve()
            try:
                resolved.relative_to(root.resolve())
            except ValueError:
                errors.append(f"{relative}:{link['line']}: link escapes repository: {target}")
                continue
            if not resolved.exists():
                errors.append(f"{relative}:{link['line']}: missing link destination {target}")
            elif parsed.fragment and resolved.is_file() and resolved.suffix.lower() in {".md",".txt"}:
                known = slugs.get(resolved)
                if known is None:
                    known = heading_slugs(resolved.read_text())
                fragment = unquote(parsed.fragment)
                if fragment not in known:
                    errors.append(f"{relative}:{link['line']}: unknown source heading #{fragment} in {decoded or relative}")
        if path.suffix.lower() == ".md":
            inventory.append({"path":relative,"sha256":hashlib.sha256(source.encode()).hexdigest(),
                              **math_table_inventory(source)})
    learning = root/"learning"
    bridges = [path for path in learning.glob("*.md") if re.search(r"(?:source|watrous)[_-]bridge",path.name,re.I)] if learning.is_dir() else []
    if len(bridges) != 1:
        errors.append(f"Expected one canonical learning source bridge; found {len(bridges)}")
    anchor = {"author":"John Watrous","title":"The Theory of Quantum Information","year":2018}
    if len(bridges) == 1:
        bridge = bridges[0].read_text()
        if not (re.search(r"\bWatrous\b",bridge) and "The Theory of Quantum Information" in bridge and "2018" in bridge):
            errors.append("Canonical source bridge does not identify selected Watrous2018 anchor")
        anchor["canonical_bridge"] = bridges[0].relative_to(root).as_posix()
    milestones = milestone_checks(learning/"MILESTONES.md",errors)
    return {"passed":not errors,"errors":errors,"relative_links_checked":links_checked,
            "selected_anchor":anchor,"milestones":milestones,"markdown_pages":inventory,
            "reader_plaintext":[path.relative_to(root).as_posix() for path in readers if path.suffix.lower() != ".md"],
            "scope":"Source navigation, declared learning fields and targeted prose hygiene only. Does not certify science, bibliography completeness, teaching quality, or hosted math/visual rendering."}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root",type=Path,default=Path(__file__).resolve().parents[1])
    parser.add_argument("--output",type=Path,help="Optional JSON report; stdout always gives the result.")
    parser.add_argument("--private-policy",type=Path,
                        help="Optional external JSON with additional prose_patterns/filename_patterns; keep private policies outside the repository.")
    arguments = parser.parse_args()
    policy = json.loads(arguments.private_policy.read_text()) if arguments.private_policy else {}
    for key in ("prose_patterns","filename_patterns"):
        if not isinstance(policy.get(key,[]),list) or not all(isinstance(item,str) for item in policy.get(key,[])):
            parser.error(f"Private policy {key} must be a list of regular-expression strings")
    result = run_checks(arguments.root.resolve(),policy.get("prose_patterns",()),policy.get("filename_patterns",()))
    result["private_policy_applied"] = bool(arguments.private_policy)
    encoded = json.dumps(result,indent=2,ensure_ascii=False)+"\n"
    if arguments.output:
        arguments.output.parent.mkdir(parents=True,exist_ok=True)
        arguments.output.write_text(encoded)
    print(encoded,end="")
    raise SystemExit(0 if result["passed"] else 1)


if __name__ == "__main__":
    main()
