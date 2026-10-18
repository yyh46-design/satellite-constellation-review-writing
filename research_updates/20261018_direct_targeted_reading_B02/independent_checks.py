"""Independent mathematical checks, not a reproduction of the paper's HHHO solver.
Source: Yin et al., DOI 10.1016/j.cja.2025.103774, Eqs. (16)-(27), Tables 3/4/8.
Run: python independent_checks.py [output.json]
Requires NumPy and SciPy. No network, author code, or third-party PDF is used.
"""
from __future__ import annotations
import json
import math
from pathlib import Path
import sys
import numpy as np
from scipy.optimize import linprog


def checked_inputs(a, budget):
    a = np.asarray(a, dtype=float)
    if a.ndim != 1 or not len(a) or not np.all(np.isfinite(a)):
        raise ValueError('a must be a nonempty finite one-dimensional array')
    if not math.isfinite(budget) or budget < 0:
        raise ValueError('budget must be finite and nonnegative')
    return a, float(budget)


def support_sort(a, budget):
    """Support of {|z_i|<=1, sum |z_i|<=budget} at a."""
    a, budget = checked_inputs(a, budget)
    b = min(budget, len(a))
    k = math.floor(b)
    s = np.sort(np.abs(a))[::-1]
    return float(s[:k].sum() + ((b-k)*s[k] if k < len(a) else 0.0))


def support_primal(a, budget):
    a, budget = checked_inputs(a, budget)
    n = len(a)
    # z = p - q, p,q >= 0; p_i+q_i<=1; sum(p+q)<=B.
    constraints = np.vstack([np.hstack([np.eye(n), np.eye(n)]), np.ones(2*n)])
    result = linprog(np.r_[-a, a], A_ub=constraints,
                     b_ub=np.r_[np.ones(n), budget], bounds=(0, None), method='highs')
    if not result.success:
        raise RuntimeError(result.message)
    return float(-result.fun)


def support_dual(a, budget):
    a, budget = checked_inputs(a, budget)
    n = len(a)
    # min B*mu + sum lambda; mu+lambda_i >= |a_i|.
    result = linprog(np.r_[budget, np.ones(n)],
                     A_ub=np.hstack([-np.ones((n, 1)), -np.eye(n)]),
                     b_ub=-np.abs(a), bounds=(0, None), method='highs')
    if not result.success:
        raise RuntimeError(result.message)
    return float(result.fun)


def main():
    rng = np.random.default_rng(20261018)
    residuals = []
    for n in [1, 2, 4, 9, 16]:
        for _ in range(4):
            a = rng.uniform(-60, 60, n)
            for b in [0.0, 0.5, 1.0, n/2, float(n), float(n+1)]:
                values = [support_sort(a,b), support_primal(a,b), support_dual(a,b)]
                residuals.append(max(values)-min(values))
    assert len(residuals) == 120
    assert max(residuals) < 1e-8
    # Mathematical invariant ensemble, NOT reconstructed paper initializations.
    theta = (np.arange(200000)+0.5)*math.pi/200000
    x = np.cos(theta)
    mapped = 4*x**3 - 3*x
    identity_error = float(np.max(np.abs(mapped-np.cos(3*theta))))
    expected_outer = 2*math.acos(0.8)/math.pi
    observed_outer = float(np.mean(np.abs(mapped)>0.8))
    assert identity_error < 1e-12
    assert abs(observed_outer-expected_outer) < 1e-4
    fuel_delivered = sum([500,200,500,300,200,400,250,450,500])
    reported_objective = 3557.1677
    table4_sum = sum([524.1902,1417.2870,1340.0238,275.6667])
    assert abs(table4_sum-reported_objective) < 1e-8
    report = {
        'scope': 'original mathematical checks only; no paper optimizer or flight replication',
        'source_doi': '10.1016/j.cja.2025.103774',
        'budget_support': {'cases':len(residuals), 'lp_solves':2*len(residuals),
          'max_absolute_difference':max(residuals), 'tolerance':1e-8,
          'fractional_example_coeff_minutes':[60,45,20,10], 'budget':1.5,
          'support_minutes':support_sort([60,45,20,10],1.5),
          'max_number_of_nonzero_deviations_is_not_budget':True},
        'cubic_map': {'identity':'4*cos(theta)^3-3*cos(theta)=cos(3*theta)',
          'max_identity_error':identity_error,
          'invariant_density':'1/(pi*sqrt(1-x*x)) on (-1,1), not uniform',
          'outer_probability_abs_x_gt_0p8':expected_outer,
          'ensemble_n':len(theta), 'mapped_ensemble_outer_probability':observed_outer,
          'uniform_outer_probability':0.2,
          'does_not_reproduce_finite_initialization_or_refute_reported_optimizer_results':True},
        'fuel_accounting': {'table3_delivered_kg':fuel_delivered,
          'table4_sum_kg':table4_sum, 'reported_total_kg':reported_objective,
          'difference_propellant_under_paper_assumptions_kg':reported_objective-fuel_delivered,
          'difference_fraction_of_total':(reported_objective-fuel_delivered)/reported_objective},
        'table8_direction_check': {'lowest_mean':'Cubic + HHHO', 'lowest_sd':'Logistic + HHHO',
          'cubic_mean_kg':8479.4671, 'logistic_mean_kg':8549.7191,
          'cubic_sd_kg':39.08, 'logistic_sd_kg':25.81,
          'no_raw_samples_no_significance_or_per_run_dominance_claim':True},
        'human_verified':False, 'paper_simulation_reproduced':False
    }
    target = Path(sys.argv[1]) if len(sys.argv)>1 else Path(__file__).with_name('independent_check_results.json')
    target.write_text(json.dumps(report, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')
    print(json.dumps(report, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
