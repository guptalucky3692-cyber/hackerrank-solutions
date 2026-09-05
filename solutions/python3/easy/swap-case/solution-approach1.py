# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/swap-case/problem?isFullScreen=true
# Problem     sWAP cASE
# Difficulty  Easy
# Subdomain   Strings
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-06-21, 03:58 p.m.
# Technique   built-in-swapcase-method
# Time        O(n)
# Space       O(n)
# Insight     The implementation leverages the native Python string method to iterate through the input once and return a new string with inverted casing for all alphabetic characters.
# Interview   Before: "I would iterate through each character and check its case using conditional logic." After: "Using the built-in swapcase method is more idiomatic and efficient, achieving O(n) time complexity while correctly handling non-alphabetic characters as specified in the problem constraints."
# Pitfalls    (1) Assuming the method modifies the original string in-place rather than returning a new string object.  (2) Overlooking that non-alphabetic characters like spaces or punctuation remain unchanged by the swapcase operation.
# ──────────────────────────────────────────────────

def swap_case(s):
    s = s.swapcase()
    return s
