# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/python-mod-divmod/problem?isFullScreen=true
# Problem     Mod Divmod
# Difficulty  Easy
# Subdomain   Math
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-06-21, 04:31 p.m.
# Technique   built-in-arithmetic-functions
# Time        O(1)
# Space       O(1)
# Insight     The solution utilizes Python's native integer division, modulo operator, and the divmod function to compute and display the quotient and remainder of two integers.
# Interview   Before: "How do I compute quotient and remainder separately?" After: "Use the // operator for integer division and % for the remainder, or the divmod function to return both in O(1) time. This handles the required output format efficiently for any two integers a and b."
# Pitfalls    (1) Confusing the float division operator / with the integer division operator // in Python 3.  (2) Failing to handle the input format correctly by reading two separate lines for a and b.
# ──────────────────────────────────────────────────

# Enter your code here. Read input from STDIN. Print output to STDOUT
a = int(input())
b = int(input())
print(a//b)
print(a%b)
print(divmod(a,b))
