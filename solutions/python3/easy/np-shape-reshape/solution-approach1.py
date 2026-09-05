# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/np-shape-reshape/problem?isFullScreen=true
# Problem     Shape and Reshape
# Difficulty  Easy
# Subdomain   Numpy
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-06-20, 01:49 p.m.
# ──────────────────────────────────────────────────

import numpy
n=list(map(int,input().split()))
print(numpy.reshape(n,(3,3)))
