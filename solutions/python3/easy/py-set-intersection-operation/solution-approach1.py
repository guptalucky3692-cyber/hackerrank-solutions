# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/py-set-intersection-operation/problem?isFullScreen=true
# Problem     Set .intersection() Operation
# Difficulty  Easy
# Subdomain   Sets
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-06-22, 01:49 p.m.
# Technique   set-intersection-cardinality
# Time        O(n + m)
# Space       O(n + m)
# Insight     The solution computes the intersection of two sets of student roll numbers and returns the count of elements present in both sets.
# Interview   Before: "I would iterate through one list and check for existence in the other." After: "Using Python's set intersection, the operation runs in O(n + m) time, which is optimal for finding common elements between two collections of size n and m."
# Pitfalls    (1) Confusing the .intersection() method with the & operator, which requires both operands to be sets.  (2) Assuming the input sets are sorted, which is not guaranteed by the problem statement.  (3) Failing to handle potential duplicate roll numbers in the input, though set conversion naturally handles this.
# ──────────────────────────────────────────────────

# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
N = set(map(int,input().split(' ')))
m = int(input())
M = set(map(int,input().split(' ')))
print(len(list(N.intersection(M))))
