# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/py-set-union/problem?isFullScreen=true
# Problem     Set .union() Operation
# Difficulty  Easy
# Subdomain   Sets
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-06-22, 01:53 p.m.
# ──────────────────────────────────────────────────

# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
N = set(map(int,input().split()))
m =int(input())
M = set(map(int,input().split()))
print(len(list(N.union(M))))
