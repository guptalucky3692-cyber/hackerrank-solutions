# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/py-introduction-to-sets/problem?isFullScreen=true
# Problem     Introduction to Sets
# Difficulty  Easy
# Subdomain   Sets
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-07-01, 10:16 p.m.
# Technique   set-deduplication-average
# Time        O(N)
# Space       O(N)
# Insight     The implementation converts the input list into a set to eliminate duplicate values before calculating the arithmetic mean of the unique elements.
# Interview   Before: "I would iterate through the list and track seen values in a dictionary to calculate the average." After: "Using a set is more idiomatic in Python, reducing the complexity to O(N) time and O(N) space while automatically handling duplicates as required by the problem."
# Pitfalls    (1) The code assumes the input variable is named arr, but the function parameter is named array, which will cause a NameError.  (2) The code references a global variable n which is not defined within the function scope, leading to a NameError.  (3) The code returns the boolean false instead of a float, which violates the return type requirement specified in the problem description.
# ──────────────────────────────────────────────────

def average(array):
    if len(arr)>n or len(arr)<n:
        return false
    return sum(set(arr))/len(set(arr))
    # your code goes here
