# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/symmetric-difference/problem?isFullScreen=true
# Problem     Symmetric Difference
# Difficulty  Easy
# Subdomain   Sets
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-06-21, 04:16 p.m.
# Technique   set-symmetric-difference-sorting
# Time        O(M + N + K log K)
# Space       O(M + N)
# Insight     The symmetric difference is computed by taking the union of the relative complements of two sets, followed by sorting the resulting collection to meet the ascending order requirement.
# Interview   Before: "I would iterate through both lists and manually track counts to find unique elements." After: "Using Python's set operations, I can compute the symmetric difference in O(M + N) time, then sort the result in O(K log K) time, where K is the number of unique elements."
# Pitfalls    (1) Failing to sort the final result, as sets are unordered collections and the problem requires ascending order.  (2) Using the wrong set operator, as the symmetric difference is specifically the union of differences, not the simple difference of the two sets.
# ──────────────────────────────────────────────────

# Enter your code here. Read input from STDIN. Print output to STDOUT
m = int(input())
M = set(map(int,input().split()))
n = int(input())
N = set(map(int,input().split()))
u = set(M).difference(N)
v = set(N).difference(M)
result  = sorted(list(u.union(v)))
for i in result:
    print(i)
  
