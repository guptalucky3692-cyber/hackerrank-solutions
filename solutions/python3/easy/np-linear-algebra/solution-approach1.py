# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/np-linear-algebra/problem?isFullScreen=true
# Problem     Linear Algebra
# Difficulty  Easy
# Subdomain   Numpy
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-06-19, 05:48 p.m.
# ──────────────────────────────────────────────────

import numpy as np
N = int(input())
A = []
for _ in range(N):
  A.append(list(map(float,input().split(' '))))
print(round(np.linalg.det(A), 2))
  
 
