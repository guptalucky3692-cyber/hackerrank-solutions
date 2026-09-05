# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/py-set-symmetric-difference-operation/problem?isFullScreen=true
# Problem     Set .symmetric_difference() Operation
# Difficulty  Easy
# Subdomain   Sets
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-07-04, 05:43 p.m.
# Technique   set-symmetric-difference-operator
# Time        O(N + M)
# Space       O(N + M)
# Insight     The symmetric difference operator computes the set of elements present in either set but not in their intersection, effectively identifying unique subscriptions.
# Interview   Before: "I would iterate through both lists and count occurrences." After: "Using the XOR operator on sets provides an O(N+M) solution, where N and M are the sizes of the two input sets, efficiently filtering out common elements."
# Pitfalls    (1) Confusing the ^ operator with the bitwise XOR on integers instead of set symmetric difference.  (2) Assuming the input sets are sorted, which is not required for the symmetric difference operation.  (3) Failing to handle potential duplicate entries in the input lists, which the set constructor automatically resolves.
# ──────────────────────────────────────────────────

# Enter your code here. Read input from STDIN. Print output to STDOU
y = int(input())
x = set(map(int,input().split()))
v = int(input())
t =  set(map(int,input().split()))
print(len(x^t))
