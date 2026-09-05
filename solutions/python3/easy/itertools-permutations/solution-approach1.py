# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/itertools-permutations/problem?isFullScreen=true
# Problem     itertools.permutations()
# Difficulty  Easy
# Subdomain   Itertools
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-07-03, 06:58 p.m.
# ──────────────────────────────────────────────────

# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import permutations
s,k = input().split()
k = int(k)
t = sorted(list(permutations(s,k)))
for x in t:
    print(''.join(x))
    
