# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/py-set-difference-operation/problem?isFullScreen=true
# Problem     Set .difference() Operation
# Difficulty  Easy
# Subdomain   Sets
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-06-22, 02:14 p.m.
# ──────────────────────────────────────────────────

# Enter your code here. Read input from STDIN. Print output to STDOUTn_eng = int(input())
num1 = int(input())
setA = set(map(int, input().split()))
num2 = int(input())
setB = set(map(int, input().split()))

print(len(setA.difference(setB)))
