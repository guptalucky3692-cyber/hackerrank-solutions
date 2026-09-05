# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/np-transpose-and-flatten/problem?isFullScreen=true
# Problem     Transpose and Flatten
# Difficulty  Easy
# Subdomain   Numpy
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-06-19, 01:38 p.m.
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
