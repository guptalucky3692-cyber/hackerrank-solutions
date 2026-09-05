# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/np-mean-var-and-std/problem?isFullScreen=true
# Problem     Mean, Var, and Std
# Difficulty  Easy
# Subdomain   Numpy
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-06-20, 01:17 p.m.
# Technique   numpy-array-aggregation
# Time        O(N*M)
# Space       O(N*M)
# Insight     The solution leverages NumPy's built-in aggregation functions to compute statistics along specified axes, ensuring efficient processing of the 2D input array.
# Interview   Before: "How would you calculate these statistics manually?" After: "Using NumPy's mean, var, and std functions reduces the complexity to O(N*M) time, as these operations iterate over the entire N by M matrix to compute the required values."
# Pitfalls    (1) Confusing the axis parameter, as axis 1 computes row-wise statistics while axis 0 computes column-wise statistics.  (2) Failing to account for the default axis=None behavior, which flattens the array before calculation.  (3) Rounding errors when printing the standard deviation, as the problem requires specific precision.
# ──────────────────────────────────────────────────

import numpy as np
n,m = map(int,input().split())
arr = []
for _ in range(n):
  arr.append(list(map(int,input().split())))
x = np.array(arr)
print(np.mean(x,axis=1))
print(np.var(x,axis=0))
print(round(np.std(x, axis=None),11))
  
