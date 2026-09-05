# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/py-check-subset/problem?isFullScreen=true
# Problem     Check Subset
# Difficulty  Easy
# Subdomain   Sets
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-06-22, 02:23 p.m.
# ──────────────────────────────────────────────────

# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
for _ in range(n):
    s = int(input())
    x = set(map(int,input().split()))
    t = int(input())
    w = set(map(int,input().split()))
    y =  x.issubset(w)
    print(y)
    
