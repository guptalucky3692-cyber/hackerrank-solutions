# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/python-print/problem?isFullScreen=true
# Problem     Print Function
# Difficulty  Easy
# Subdomain   Introduction
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-06-14, 02:26 p.m.
# Technique   range-iteration-with-end-parameter
# Time        O(n)
# Space       O(1)
# Insight     The implementation iterates through the range from one to n inclusive, printing each integer sequentially without a trailing newline or space by overriding the default end parameter.
# Interview   Before: "I would convert the range to a string and join it." After: "I used a loop with the end parameter set to an empty string to achieve O(n) time and O(1) space, ensuring no extra characters are printed between integers as required by the problem constraints."
# Pitfalls    (1) Using the default print end parameter adds a newline character after every integer, violating the requirement to print the sequence as a single string.  (2) Using range(n) instead of range(1, n + 1) results in printing integers from zero to n-1, failing to include the final integer n.
# ──────────────────────────────────────────────────

if __name__ == '__main__':
    n = int(input())
    for i in range(1,n+1):
      print(i,sep='',end='')
