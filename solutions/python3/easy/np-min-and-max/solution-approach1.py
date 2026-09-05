# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/np-min-and-max/problem?isFullScreen=true
# Problem     Min and Max
# Difficulty  Easy
# Subdomain   Numpy
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-06-20, 12:58 p.m.
# ──────────────────────────────────────────────────

import numpy as np
n,m = map(int,input().split())
arr = []
for _ in range(n):
  x = list(map(int,input().split()))
  arr.append(x)
print(np.max(np.min(arr,axis=1)))


