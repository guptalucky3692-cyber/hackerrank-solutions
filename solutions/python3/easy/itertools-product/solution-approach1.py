# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/itertools-product/problem?isFullScreen=true
# Problem     itertools.product()
# Difficulty  Easy
# Subdomain   Itertools
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-07-03, 06:50 p.m.
# Technique   itertools-cartesian-product
# Time        O(N * M)
# Space       O(N * M)
# Insight     The itertools.product function generates the Cartesian product of input iterables by effectively performing nested loops over the provided sequences.
# Interview   Before: "I would use nested loops to generate all pairs." After: "Using itertools.product is more idiomatic and efficient in Python, yielding an O(N * M) time and space complexity where N and M are the lengths of the input lists."
# Pitfalls    (1) Passing map objects directly to product works in Python 3, but consuming them before passing to product would result in an empty output.  (2) Printing the result using the unpack operator * with a space separator is required to match the specific output format of space-separated tuples.
# ──────────────────────────────────────────────────

# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import product
a = map(int,input().split())
b= map(int,input().split())
c = list(product(a,b))
print(*c, sep=" ")
