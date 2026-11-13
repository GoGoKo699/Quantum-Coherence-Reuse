#!/usr/bin/env python3
"""Finite diagnostics for a returned-reference coherent pair processor.

The direct processor checks construct and evolve complete finite Hilbert-space
matrices.  The separate classical-sector calculation is a cross-check and
collective benchmark, rather than the source of the evolved states.  All
numbers are floating point; the analytical claims are proved in science/.
"""
from __future__ import annotations

import argparse
import json
import math
import platform
from pathlib import Path

import numpy as np
import scipy
from scipy.linalg import eigvalsh
from scipy.stats import binom

TOLERANCE = 5e-11


def reference_profile(ladder_parameter: int) -> np.ndarray:
    if ladder_parameter < 3:
        raise ValueError("L must be at least three")
    j = np.arange(1, ladder_parameter, dtype=float)
    return 8/(3*ladder_parameter)*np.sin(np.pi*j/ladder_parameter)**4


def conserving_pair_processor(ladder_parameter: int):
    probabilities = reference_profile(ladder_parameter)
    reference = np.sqrt(probabilities)
    dimension = len(reference)
    pair_charges = np.array([0, 1, 1, 2])
    charges = np.array([r+q for r in range(dimension) for q in pair_charges])
    desired = np.kron(reference, np.ones(4)/2)
    unitary = np.zeros((4*dimension, 4*dimension), dtype=float)
    for charge in sorted(set(charges)):
        indices = np.flatnonzero(charges == charge)
        block = np.eye(len(indices))
        initial_reference_charge = charge-1
        if 0 <= initial_reference_charge < dimension:
            initial = np.zeros(len(indices))
            initial_index = 4*initial_reference_charge+1  # |r,01>
            initial[np.flatnonzero(indices == initial_index)[0]] = 1
            target = desired[indices]
            target = target/np.linalg.norm(target)
            difference = initial-target
            if np.linalg.norm(difference) > 1e-14:
                block -= 2*np.outer(difference, difference)/(difference@difference)
        unitary[np.ix_(indices, indices)] = block
    return probabilities, reference, unitary, charges


def trace_distance_density(first: np.ndarray, second: np.ndarray) -> float:
    difference = first-second
    difference = (difference+difference.conj().T)/2
    return float(np.abs(eigvalsh(difference)).sum()/2)


def trace_distance_vectors(first: np.ndarray, second: np.ndarray) -> float:
    # Deliberately evaluate the full density-matrix difference, independently
    # from the charge-sector overlap formula.
    return trace_distance_density(np.outer(first, first.conj()),
                                  np.outer(second, second.conj()))


def apply_pair(vector, unitary, dimension, qubit_count, first_qubit):
    axes = [0, first_qubit+1, first_qubit+2]
    rest = [axis for axis in range(qubit_count+1) if axis not in axes]
    permutation = axes+rest
    inverse = np.argsort(permutation)
    tensor = vector.reshape([dimension]+[2]*qubit_count)
    matrix = tensor.transpose(permutation).reshape(4*dimension, -1)
    changed = (unitary@matrix).reshape([dimension,2,2]+[2]*(qubit_count-2))
    return changed.transpose(inverse).reshape(-1)


def embedded_pair_unitary(unitary, dimension, qubit_count, first_qubit):
    total = dimension*2**qubit_count
    columns = []
    for j in range(total):
        column = np.zeros(total)
        column[j] = 1
        columns.append(apply_pair(column, unitary, dimension,
                                  qubit_count, first_qubit))
    return np.stack(columns, axis=1)


def exact_sector_benchmark(probabilities, qubit_count):
    if qubit_count < 2 or qubit_count % 2:
        raise ValueError("N must be a positive even integer")
    half = qubit_count//2
    centered_binomial = binom.pmf(np.arange(qubit_count+1), qubit_count, .5)
    target_sector = np.convolve(probabilities, centered_binomial)
    initial_sector = np.pad(probabilities, (half, half))
    h_squared = float(np.sum((np.sqrt(initial_sector)-np.sqrt(target_sector))**2))
    overlap = float(np.dot(np.sqrt(initial_sector), np.sqrt(target_sector)))
    # Stable equivalent of sqrt(1-B^2), including very small errors.
    distance = math.sqrt(max(0., h_squared*(1-h_squared/4)))
    return {'overlap':overlap, 'hellinger_squared':h_squared,
            'conserving_collective_trace_distance':distance}


def profile_checks():
    maximum_normalization = 0.
    maximum_mean_error = 0.
    maximum_identity_residual = 0.
    maximum_second_difference_ratio = 0.
    maximum_hellinger_ratio = 0.
    for ladder_parameter in range(3, 130):
        p = reference_profile(ladder_parameter)
        theta = np.pi/ladder_parameter
        a = np.sin(theta)**2
        x = np.arange(1,ladder_parameter)*theta
        f = np.sin(x)**4
        differences = np.sin(x-theta)**4-2*f+np.sin(x+theta)**4
        identity = 2*a*(np.cos(2*x)-(1-a)*np.cos(4*x))
        ratio = np.abs(differences)/(14*a*np.sin(x)**2)
        q = np.convolve(p, np.array([.25,.5,.25]))
        p_extended = np.pad(p, (1,1))
        h_squared = float(np.sum((np.sqrt(p_extended)-np.sqrt(q))**2))
        analytical = 98/3*a*a
        mean = float(np.dot(np.arange(len(p)),p))
        maximum_normalization = max(maximum_normalization, abs(p.sum()-1))
        maximum_mean_error = max(maximum_mean_error, abs(mean-(ladder_parameter/2-1)))
        maximum_identity_residual = max(maximum_identity_residual,
                                        float(np.max(np.abs(differences-identity))))
        maximum_second_difference_ratio = max(maximum_second_difference_ratio,
                                              float(np.max(ratio)))
        maximum_hellinger_ratio = max(maximum_hellinger_ratio, h_squared/analytical)
        assert abs(p.sum()-1) < TOLERANCE
        assert abs(mean-(ladder_parameter/2-1)) < TOLERANCE
        assert np.max(ratio) <= 1+TOLERANCE
        assert h_squared <= analytical+TOLERANCE
        # The sum over the two exterior sites must be included in Hellinger.
        exterior = q[0]+q[-1]
        assert abs(exterior-(8/(3*ladder_parameter))*a*a/2) < TOLERANCE
    return {'L_first':3,'L_last':129,'profiles_tested':127,
        'maximum_normalization_error':maximum_normalization,
        'maximum_mean_excitation_error':maximum_mean_error,
        'maximum_second_difference_identity_residual':maximum_identity_residual,
        'maximum_second_difference_to_proved_bound_ratio':maximum_second_difference_ratio,
        'maximum_hellinger_squared_to_proved_bound_ratio':maximum_hellinger_ratio}


def direct_reuse_case(ladder_parameter, pair_count):
    p, reference, unitary, charges = conserving_pair_processor(ladder_parameter)
    dimension = len(reference)
    qubit_count = 2*pair_count
    register = np.zeros(2**qubit_count)
    register[int('01'*pair_count,2)] = 1
    vector = np.kron(reference, register)
    pair_initial = np.kron(reference,np.array([0.,1.,0.,0.]))
    pair_target = np.kron(reference,np.ones(4)/2)
    pair_error = trace_distance_vectors(unitary@pair_initial,pair_target)
    pair_sector = exact_sector_benchmark(p,2)
    assert abs(pair_error-pair_sector['conserving_collective_trace_distance']) < TOLERANCE
    records = []
    for processed in range(1,pair_count+1):
        vector = apply_pair(vector,unitary,dimension,qubit_count,2*(processed-1))
        ideal_register = np.ones(4**processed)/2**processed
        for _ in range(pair_count-processed):
            ideal_register = np.kron(ideal_register,np.array([0.,1.,0.,0.]))
        ideal = np.kron(reference,ideal_register)
        distance = trace_distance_vectors(vector,ideal)
        benchmark = exact_sector_benchmark(p,2*processed)
        records.append({'pairs_processed':processed,
            'full_joint_trace_distance':distance,
            'hybrid_upper':processed*pair_error,
            'collective_optimum_for_same_reference':benchmark['conserving_collective_trace_distance']})
        assert distance <= processed*pair_error+TOLERANCE
        assert distance+TOLERANCE >= benchmark['conserving_collective_trace_distance']
    charge_matrix = np.diag(charges)
    unitarity = float(np.linalg.norm(unitary.T@unitary-np.eye(4*dimension),ord=2))
    conservation = float(np.linalg.norm(unitary@charge_matrix-charge_matrix@unitary,ord=2))
    state_norm = float(abs(np.vdot(vector,vector)-1))
    mean = float(np.dot(np.arange(dimension),p))
    variance = float(np.dot(np.arange(dimension)**2,p)-mean**2)
    assert unitarity < TOLERANCE and conservation < TOLERANCE and state_norm < TOLERANCE
    return {'L':ladder_parameter,'reference_levels':dimension,
        'reference_mean_excitation':mean,'reference_variance':variance,
        'pair_count':pair_count,'same_pair_matrix_reused':True,
        'pair_error_from_full_density_matrix':pair_error,
        'pair_error_from_sector_benchmark':pair_sector['conserving_collective_trace_distance'],
        'unitarity_spectral_residual':unitarity,
        'charge_commutator_spectral_residual':conservation,
        'final_state_normalization_error':state_norm,'stages':records}


def scaling_and_rounding_checks():
    rows = []
    for qubit_count in [2,8,32,128]:
        for error_budget in [.2,.05,.01]:
            ladder_parameter = math.ceil(math.sqrt(29*qubit_count/error_budget))
            p = reference_profile(ladder_parameter)
            pair_error = exact_sector_benchmark(p,2)['conserving_collective_trace_distance']
            hybrid = qubit_count/2*pair_error
            analytical = 7/np.sqrt(6)*qubit_count*np.sin(np.pi/ladder_parameter)**2
            collective = exact_sector_benchmark(p,qubit_count)['conserving_collective_trace_distance']
            mean = ladder_parameter/2-1
            lower = .25*(-np.expm1(-qubit_count/(256*(mean+1)**2)))
            assert ladder_parameter >= 3
            assert collective <= hybrid+TOLERANCE
            assert hybrid <= analytical+TOLERANCE
            assert analytical <= error_budget+TOLERANCE
            assert collective+TOLERANCE >= lower
            rows.append({'N':qubit_count,'error_budget':error_budget,
                'L_ceiling':ladder_parameter,'reference_mean_excitation':mean,
                'pair_error':pair_error,'hybrid_upper':hybrid,
                'analytical_upper':float(analytical),
                'collective_same_reference_error':collective,
                'universal_converse_at_this_mean_energy':float(lower)})
    return rows


def finite_noise_check():
    ladder_parameter = 12
    pairs = 2
    eta, zeta = .02,.01
    p, reference, unitary, _ = conserving_pair_processor(ladder_parameter)
    dimension = len(reference)
    nominal_reference = np.outer(reference,reference)
    ground = np.zeros(dimension);ground[0]=1
    prepared_reference = (1-eta)*nominal_reference+eta*np.outer(ground,ground)
    measured_eta = trace_distance_density(prepared_reference,nominal_reference)
    register = np.zeros(4**pairs);register[int('01'*pairs,2)]=1
    rho = np.kron(prepared_reference,np.outer(register,register))
    for first_qubit in [0,2]:
        embedded = embedded_pair_unitary(unitary,dimension,2*pairs,first_qubit)
        # This mixture of ideal U and identity has half-diamond distance <=zeta.
        rho = (1-zeta)*(embedded@rho@embedded.T)+zeta*rho
    plus = np.ones(4**pairs)/2**pairs
    output = np.outer(plus,plus)
    distance_nominal = trace_distance_density(rho,np.kron(nominal_reference,output))
    distance_prepared = trace_distance_density(rho,np.kron(prepared_reference,output))
    pair_error = exact_sector_benchmark(p,2)['conserving_collective_trace_distance']
    nominal_bound = measured_eta+pairs*zeta+pairs*pair_error
    prepared_bound = 2*measured_eta+pairs*zeta+pairs*pair_error
    assert measured_eta <= eta+TOLERANCE
    assert distance_nominal <= nominal_bound+TOLERANCE
    assert distance_prepared <= prepared_bound+TOLERANCE
    return {'L':ladder_parameter,'pairs':pairs,'preparation_mixture_weight':eta,
        'actual_preparation_trace_error':measured_eta,
        'per_use_half_diamond_sufficient_upper':zeta,
        'actual_nominal_product_target_error':distance_nominal,
        'nominal_product_target_upper':nominal_bound,
        'actual_prepared_reference_product_target_error':distance_prepared,
        'prepared_reference_product_target_upper':prepared_bound,
        'noise_model':'At each use independently mix the ideal pair unitary with identity. The proved bound does not assume this independence.'}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',type=Path,default=Path(__file__).with_name('results.json'))
    arguments = parser.parse_args()
    result = {'passed':True,
        'runtime':{'python':platform.python_version(),'numpy':np.__version__,'scipy':scipy.__version__},
        'profile_checks':profile_checks(),
        'direct_matrix_cases':[direct_reuse_case(3,1),direct_reuse_case(4,2),
                               direct_reuse_case(8,3),direct_reuse_case(16,3)],
        'scaling_and_rounding':scaling_and_rounding_checks(),
        'finite_noise_check':finite_noise_check(),
        'scope':'Finite floating-point diagnostics. Full matrix evolution checks the selected processors and global trace distances; theorems are analytical. No interval certificate, hardware realization, optimized constants, or physical control-cost claim.'}
    arguments.output.parent.mkdir(parents=True,exist_ok=True)
    arguments.output.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'passed':True,'output':str(arguments.output),
        'profiles_tested':result['profile_checks']['profiles_tested'],
        'direct_matrix_cases':len(result['direct_matrix_cases']),
        'rounding_cases':len(result['scaling_and_rounding'])},indent=2))


if __name__ == '__main__':
    main()
