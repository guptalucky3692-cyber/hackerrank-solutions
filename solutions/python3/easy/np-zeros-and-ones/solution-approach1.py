# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/np-zeros-and-ones/problem?isFullScreen=true
# Problem     Zeros and Ones
# Difficulty  Easy
# Subdomain   Numpy
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-06-20, 12:32 p.m.
# ──────────────────────────────────────────────────

import numpy as np
x  = list(map(int,input().split()))
print(np.zeros((x),dtype= int))
print(np.ones((x),dtype= int))

    
