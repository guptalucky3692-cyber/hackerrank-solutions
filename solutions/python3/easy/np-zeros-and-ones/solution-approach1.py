# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/np-zeros-and-ones/problem?isFullScreen=true
# Problem     Zeros and Ones
# Difficulty  Easy
# Subdomain   Numpy
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-06-20, 12:32 p.m.
# Technique   numpy-array-initialization
# Time        O(N)
# Space       O(N)
# Insight     The code converts space-separated input into a tuple of integers to define the dimensions for numpy array creation functions.
# Interview   Before: "How do I create a multi-dimensional array of zeros or ones in NumPy?" After: "You pass the shape tuple to numpy.zeros or numpy.ones with dtype=int, resulting in O(N) time and space complexity where N is the total number of elements."
# Pitfalls    (1) Failing to specify dtype=int results in default float values, which violates the integer type requirement.  (2) Passing the input list directly as a tuple is required because numpy functions expect a shape sequence.
# ──────────────────────────────────────────────────

import numpy as np
x  = list(map(int,input().split()))
print(np.zeros((x),dtype= int))
print(np.ones((x),dtype= int))

    
