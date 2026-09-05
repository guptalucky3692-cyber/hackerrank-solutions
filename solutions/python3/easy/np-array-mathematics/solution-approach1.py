# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/np-array-mathematics/problem?isFullScreen=true
# Problem     Array Mathematics
# Difficulty  Easy
# Subdomain   Numpy
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-06-14, 03:24 p.m.
# ──────────────────────────────────────────────────

import numpy
N, M = map(int, input().split())
A = []
B = []

for i in range(N):
    arr = list(map(int ,input().split()))
    A.append(arr)
    
for i in range(N):
    arr = list(map(int ,input().split()))
    B.append(arr)

A = numpy.array(A, int)
B = numpy.array(B, int)

# Add (+)
print(A+B)

# Subtract (-)
print(A-B)

# Multiply (*)
print(A*B)

# Integer Division (/)
#print(A/B)
print(numpy.floor_divide(A,B))

# Mod %
print(A%B)

# Power (**)
print(A**B)
