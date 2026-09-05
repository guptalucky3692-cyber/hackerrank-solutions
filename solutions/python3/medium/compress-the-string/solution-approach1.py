# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/compress-the-string/problem?isFullScreen=true
# Problem     Compress the String! 
# Difficulty  Medium
# Subdomain   Itertools
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-06-23, 01:54 p.m.
# ──────────────────────────────────────────────────

# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import groupby 

s = input()
L = []

for key, group in groupby(s):
    L.append((len(list(group)), int(key)))

print(*L)
