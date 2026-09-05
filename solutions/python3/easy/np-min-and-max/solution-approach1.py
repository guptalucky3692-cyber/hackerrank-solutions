# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/np-min-and-max/problem?isFullScreen=true
# Problem     Min and Max
# Difficulty  Easy
# Subdomain   Numpy
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-06-20, 12:58 p.m.
# Technique   numpy-axis-reduction
# Time        O(N*M)
# Space       O(N*M)
# Insight     The solution computes the minimum value across each row of the N by M matrix and subsequently identifies the maximum value among those row-wise minima.
# Interview   Before: "I would iterate through each row to find the minimum, then track the global maximum." After: "Using NumPy's axis-specific reduction, I perform the min operation on axis 1 and then the max operation on the result, achieving O(N*M) time complexity for an N by M input array."
# Pitfalls    (1) Confusing axis 0 (column-wise) with axis 1 (row-wise) leads to incorrect reduction results.  (2) Failing to import the numpy library prevents the use of the required min and max array methods.  (3) Incorrectly parsing the input dimensions N and M can cause index errors when constructing the array.
# ──────────────────────────────────────────────────

import numpy as np
n,m = map(int,input().split())
arr = []
for _ in range(n):
  x = list(map(int,input().split()))
  arr.append(x)
print(np.max(np.min(arr,axis=1)))


