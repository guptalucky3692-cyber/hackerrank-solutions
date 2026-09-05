# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/symmetric-difference/problem?isFullScreen=true
# Problem     Symmetric Difference
# Difficulty  Easy
# Subdomain   Sets
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-06-21, 04:16 p.m.
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
  
