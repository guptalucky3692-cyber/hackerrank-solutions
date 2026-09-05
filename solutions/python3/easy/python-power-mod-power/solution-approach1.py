# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/python-power-mod-power/problem?isFullScreen=true
# Problem     Power - Mod Power
# Difficulty  Easy
# Subdomain   Math
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-06-22, 02:28 p.m.
# Technique   built-in-modular-exponentiation
# Time        O(log b)
# Space       O(1)
# Insight     The implementation utilizes Python's built-in pow function to perform standard exponentiation and efficient modular exponentiation.
# Interview   Before: "I would use a loop to multiply the base b times." After: "Using the built-in pow(a, b, m) is more efficient, operating in O(log b) time, and correctly handles the modular exponentiation requirement specified in the problem constraints."
# Pitfalls    (1) Using math.pow instead of the built-in pow function, which returns a float and may cause precision issues for large integers.  (2) Providing a negative exponent as the second argument when the third argument m is present, which violates the problem's constraint that b cannot be negative.
# ──────────────────────────────────────────────────

# Enter your code here. Read input from STDIN. Print output to STDOUT
a = int(input())
b = int(input())
m = int(input())
print(pow(a,b))
print(pow(a,b,m))
