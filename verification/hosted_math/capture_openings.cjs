#!/usr/bin/env node
'use strict';
// Supplemental viewport screenshots; the canonical full-page/math collector is unchanged.
const fs=require('fs');
const path=require('path');
const {chromium}=require('playwright');
(async()=>{
 const root=process.argv[2];
 if(!root)throw new Error('Usage: node capture_openings.cjs CAPTURE_DIRECTORY');
 const report=JSON.parse(fs.readFileSync(path.join(root,'hosted-report.json'),'utf8'));
 if(report.status!=='pass')throw new Error('A passing canonical capture is required first');
 const pages=['learning/MILESTONES.md','learning/TUTORIAL.md','learning/WATROUS_BRIDGE.md','science/converse.md'];
 const browser=await chromium.launch({headless:true});const observations=[];
 try{
  for(const width of [1440,760]){
   const context=await browser.newContext({viewport:{width,height:1000}});
   for(const source of pages){
    const boundary=report.boundaries.find(x=>x.path===source);
    if(!boundary)throw new Error('Missing source boundary: '+source);
    const page=await context.newPage();
    const response=await page.goto(boundary.url,{waitUntil:'domcontentloaded',timeout:60000});
    if(response.status()!==200||page.url()!==boundary.url)throw new Error('Pinned-page navigation failed');
    await page.locator('article.markdown-body').waitFor({state:'visible'});
    await page.waitForFunction(expected=>{
     const hosts=[...document.querySelectorAll('article.markdown-body math-renderer')];
     return hosts.length===expected&&hosts.every(h=>h.querySelector('math'));
    },boundary.source_expressions,{timeout:30000});
    // A newly opened page has no lazy-load scroll cycle or stale sticky-toolbar state.
    const geometry=await page.locator('article.markdown-body h1').first().evaluate(h=>{
     const b=h.getBoundingClientRect();return {text:h.textContent,x:b.x,y:b.y,width:b.width,height:b.height,scroll_y:window.scrollY};
    });
    const name='opening-'+String(report.required_pages.indexOf(source)+1).padStart(4,'0')+'-'+width+'.png';
    await page.screenshot({path:path.join(root,name),fullPage:false});
    observations.push({path:source,width,revision:report.revision,source_sha256:boundary.source_sha256,url:boundary.url,observed_at:new Date().toISOString(),geometry,screenshot:name});
    await page.close();
   }
   await context.close();
  }
 }finally{await browser.close();}
 fs.writeFileSync(path.join(root,'openings-report.json'),JSON.stringify({kind:'hosted_openings',repository:report.repository,revision:report.revision,tree:report.tree,observations,limits:'Supplemental actual viewport captures for visual title inspection; not a substitute for the canonical mathematics report.'},null,2)+'\n');
 console.log(JSON.stringify({opening_captures:observations.length,revision:report.revision}));
})().catch(e=>{console.error(e.stack||String(e));process.exit(1);});
