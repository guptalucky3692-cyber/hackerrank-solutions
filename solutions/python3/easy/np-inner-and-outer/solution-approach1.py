# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/np-inner-and-outer/problem?isFullScreen=true
# Problem     Inner and Outer
# Difficulty  Easy
# Subdomain   Numpy
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-06-19, 05:09 p.m.
# ──────────────────────────────────────────────────

import numpy as np
A = np.array(list(map(int,input().split())))
B =  np.array(list(map(int,input().split())))
print(np.inner(A,B))
print(np.outer(A,B))



