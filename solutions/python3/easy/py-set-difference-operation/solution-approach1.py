# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/py-set-difference-operation/problem?isFullScreen=true
# Problem     Set .difference() Operation
# Difficulty  Easy
# Subdomain   Sets
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-06-22, 02:14 p.m.
# Technique   set-difference-operation
# Time        O(N + M)
# Space       O(N + M)
# Insight     The code calculates the cardinality of the relative complement of the French newspaper set within the English newspaper set using the built-in set difference method.
# Interview   Before: "How would you find unique elements in one set not present in another?" After: "I used the .difference() method, which runs in O(N + M) time, where N and M are the sizes of the two sets, to efficiently isolate the English-only subscribers."
# Pitfalls    (1) Confusing the .difference() method with the symmetric difference operator, which would include elements unique to both sets.  (2) Assuming the input sets are ordered, as set operations in Python do not preserve the original insertion order of elements.
# ──────────────────────────────────────────────────

# Enter your code here. Read input from STDIN. Print output to STDOUTn_eng = int(input())
num1 = int(input())
setA = set(map(int, input().split()))
num2 = int(input())
setB = set(map(int, input().split()))

print(len(setA.difference(setB)))
