# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/np-transpose-and-flatten/problem?isFullScreen=true
# Problem     Transpose and Flatten
# Difficulty  Easy
# Subdomain   Numpy
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-06-19, 01:38 p.m.
# Technique   numpy-array-manipulation
# Time        O(N*M)
# Space       O(N*M)
# Insight     The solution constructs a NumPy array from nested lists and utilizes built-in methods to perform matrix transposition and flattening operations.
# Interview   Before: "How would you transform a 2D matrix into its transpose and a 1D array?" After: "I use NumPy's transpose and flatten methods, which operate in O(N*M) time and space, where N and M are the dimensions of the input matrix."
# Pitfalls    (1) Failing to handle the input dimensions N and M correctly when constructing the initial list of lists.  (2) Assuming the input matrix is square, which is not guaranteed by the problem statement.  (3) Confusing the return type of numpy.transpose with the original array object.
# ──────────────────────────────────────────────────

import numpy as np
n,m= map(int,input().split())
matrix = []
for _ in range(n):
  row = list(map(int,input().split()))
  matrix.append(row)
arr = np.array(matrix)
print(arr.transpose())
print(arr.flatten())
