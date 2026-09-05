# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/itertools-permutations/problem?isFullScreen=true
# Problem     itertools.permutations()
# Difficulty  Easy
# Subdomain   Itertools
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-07-03, 06:58 p.m.
# Technique   itertools-permutations-lexicographic-sort
# Time        O(N! / (N-K)!)
# Space       O(N! / (N-K)!)
# Insight     The code generates all permutations of length k from the input string and sorts them lexicographically to satisfy the output requirement.
# Interview   Before: "I would implement a recursive backtracking algorithm to generate permutations." After: "Using itertools.permutations is more efficient, yielding O(P(N, K)) time and space complexity, while ensuring the lexicographic order required by the problem statement."
# Pitfalls    (1) Failing to sort the input string or the resulting permutations, which violates the lexicographic order requirement.  (2) Forgetting to join the tuple elements into a single string, which results in printing tuples instead of the required string format.  (3) Assuming the input string is already sorted, which is not guaranteed by the problem statement.
# ──────────────────────────────────────────────────

# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import permutations
s,k = input().split()
k = int(k)
t = sorted(list(permutations(s,k)))
for x in t:
    print(''.join(x))
    
