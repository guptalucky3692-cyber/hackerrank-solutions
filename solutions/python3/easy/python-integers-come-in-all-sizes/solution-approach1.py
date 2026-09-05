# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/python-integers-come-in-all-sizes/problem?isFullScreen=true
# Problem     Integers Come In All Sizes
# Difficulty  Easy
# Subdomain   Math
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-06-22, 02:31 p.m.
# Technique   arbitrary-precision-arithmetic
# Time        O(log b + log d)
# Space       O(log(a^b + c^d))
# Insight     Python automatically handles arbitrarily large integers, allowing direct computation of exponentiation results that exceed standard 64-bit integer limits.
# Interview   Before: "How would you handle integer overflow for a^b + c^d?" After: "Python's native integer type supports arbitrary precision, so the result is computed directly in O(log b + log d) time without overflow concerns, even when values exceed 2^63 - 1."
# Pitfalls    (1) Assuming standard 64-bit integer limits apply, which would cause overflow in languages like C++ or Java.  (2) Attempting to use modular exponentiation when the problem requires the full, unreduced sum.
# ──────────────────────────────────────────────────

# Enter your code here. Read input from STDIN. Print output to STDOUT
a =int(input())
b =int(input())
c =int(input())
d =int(input())
s = pow(a,b) + pow(c,d)
print(s)
