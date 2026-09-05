# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/np-linear-algebra/problem?isFullScreen=true
# Problem     Linear Algebra
# Difficulty  Easy
# Subdomain   Numpy
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-06-19, 05:48 p.m.
# Technique   numpy-linalg-determinant-calculation
# Time        O(N^3)
# Space       O(N^2)
# Insight     The implementation leverages the optimized NumPy linear algebra library to compute the determinant of an N by N matrix in cubic time.
# Interview   Before: "I would implement Gaussian elimination to find the determinant." After: "Using numpy.linalg.det is more efficient and idiomatic for Python, providing O(N^3) performance while handling floating-point precision automatically for square matrices."
# Pitfalls    (1) Failing to round the result to two decimal places as explicitly required by the problem statement.  (2) Assuming the input matrix is always square, though the problem statement guarantees N by N dimensions.  (3) Using integer division or improper float conversion when parsing the input matrix elements.
# ──────────────────────────────────────────────────

import numpy as np
N = int(input())
A = []
for _ in range(N):
  A.append(list(map(float,input().split(' '))))
print(round(np.linalg.det(A), 2))
  
 
