# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/np-shape-reshape/problem?isFullScreen=true
# Problem     Shape and Reshape
# Difficulty  Easy
# Subdomain   Numpy
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-06-20, 01:49 p.m.
# Technique   numpy-array-reshape
# Time        O(N)
# Space       O(N)
# Insight     The code converts a flat list of integers into a 3x3 NumPy array using the reshape function.
# Interview   Before: "I would iterate through the list and manually construct a nested list structure." After: "Using numpy.reshape provides an O(N) time and O(N) space solution that efficiently maps the flat input into the required 3x3 matrix format."
# Pitfalls    (1) Passing a list that does not contain exactly nine integers will cause a ValueError during the reshape operation.  (2) Failing to import the numpy library will result in a NameError when calling the reshape function.
# ──────────────────────────────────────────────────

import numpy
n=list(map(int,input().split()))
print(numpy.reshape(n,(3,3)))
