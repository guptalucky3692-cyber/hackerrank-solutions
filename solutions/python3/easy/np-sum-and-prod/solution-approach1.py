# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/np-sum-and-prod/problem?isFullScreen=true
# Problem     Sum and Prod
# Difficulty  Easy
# Subdomain   Numpy
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-06-20, 12:49 p.m.
# Technique   numpy-sum-prod-reduction
# Time        O(N*M)
# Space       O(N*M)
# Insight     The implementation computes the column-wise sum of the input matrix using numpy.sum and subsequently calculates the product of the resulting array elements.
# Interview   Before: "How would you aggregate a 2D array across axes?" After: "I would use numpy.sum with axis=0 to collapse rows, then apply numpy.prod to the result. This approach runs in O(N*M) time, where N and M are the dimensions of the input matrix."
# Pitfalls    (1) Confusing axis=0 (column-wise) with axis=1 (row-wise) operations.  (2) Assuming the input array is already a numpy object before calling sum or prod methods.  (3) Neglecting that numpy.prod defaults to the product of all elements when axis is None.
# ──────────────────────────────────────────────────

import numpy as np
n,m = map(int,input().split())
x = []
for _ in range(n):
  arr = list(map(int,input().split()))
  x.append(arr)
  y = np.sum(x,axis=0)
print(np.prod(y,axis= None))
  


