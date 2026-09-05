# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/np-array-mathematics/problem?isFullScreen=true
# Problem     Array Mathematics
# Difficulty  Easy
# Subdomain   Numpy
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-06-14, 03:24 p.m.
# Technique   numpy-element-wise-arithmetic
# Time        O(N*M)
# Space       O(N*M)
# Insight     The implementation leverages NumPy's vectorized element-wise arithmetic operators to perform operations on two-dimensional integer arrays in constant time relative to the number of elements.
# Interview   Before: "I would iterate through every element using nested loops to perform these calculations." After: "Using NumPy's vectorized operations, I can perform these calculations in O(N*M) time, which is significantly more efficient and readable for large arrays."
# Pitfalls    (1) Using standard division instead of numpy.floor_divide results in floating-point outputs, violating the integer requirement for the division operation.  (2) Failing to convert input lists into numpy arrays prevents the use of element-wise operator overloading.  (3) Assuming standard Python list arithmetic, which concatenates or repeats lists rather than performing element-wise mathematical operations.
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
