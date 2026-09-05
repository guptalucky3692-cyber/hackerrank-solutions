# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/compress-the-string/problem?isFullScreen=true
# Problem     Compress the String! 
# Difficulty  Medium
# Subdomain   Itertools
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-06-23, 01:54 p.m.
# Technique   itertools-groupby-aggregation
# Time        O(N)
# Space       O(N)
# Insight     The groupby function partitions the input string into contiguous segments of identical characters, allowing the length of each segment and the character value to be extracted as a tuple.
# Interview   Before: "How would you count consecutive character occurrences efficiently?" After: "Using itertools.groupby, we can group identical consecutive characters in O(N) time and O(N) space, which is optimal for the 10^4 constraint."
# Pitfalls    (1) Failing to convert the groupby key from a string to an integer, which violates the requirement to output the character as an integer.  (2) Forgetting to unpack the list of tuples using the asterisk operator, which results in an incorrect output format containing brackets and commas.
# ──────────────────────────────────────────────────

# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import groupby 

s = input()
L = []

for key, group in groupby(s):
    L.append((len(list(group)), int(key)))

print(*L)
