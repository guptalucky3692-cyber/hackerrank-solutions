# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/np-sum-and-prod/problem?isFullScreen=true
# Problem     Sum and Prod
# Difficulty  Easy
# Subdomain   Numpy
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-06-20, 12:49 p.m.
# ──────────────────────────────────────────────────

import numpy as np
n,m = map(int,input().split())
x = []
for _ in range(n):
  arr = list(map(int,input().split()))
  x.append(arr)
  y = np.sum(x,axis=0)
print(np.prod(y,axis= None))
  


