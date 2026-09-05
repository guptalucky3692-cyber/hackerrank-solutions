# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/py-set-symmetric-difference-operation/problem?isFullScreen=true
# Problem     Set .symmetric_difference() Operation
# Difficulty  Easy
# Subdomain   Sets
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-07-04, 05:43 p.m.
# ──────────────────────────────────────────────────

# Enter your code here. Read input from STDIN. Print output to STDOU
y = int(input())
x = set(map(int,input().split()))
v = int(input())
t =  set(map(int,input().split()))
print(len(x^t))
