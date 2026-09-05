# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/np-mean-var-and-std/problem?isFullScreen=true
# Problem     Mean, Var, and Std
# Difficulty  Easy
# Subdomain   Numpy
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-06-20, 01:17 p.m.
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
  
