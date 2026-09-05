# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/py-set-union/problem?isFullScreen=true
# Problem     Set .union() Operation
# Difficulty  Easy
# Subdomain   Sets
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-06-22, 01:53 p.m.
# Technique   set-union-cardinality
# Time        O(n + m)
# Space       O(n + m)
# Insight     The union operation combines two sets of student roll numbers into a single set, automatically handling duplicates to represent the total count of unique subscribers.
# Interview   Before: "I would iterate through both lists and manually check for duplicates using a hash map." After: "Using Python's built-in set union is more efficient, providing O(n + m) time complexity and O(n + m) space complexity to handle the union of two sets of size n and m."
# Pitfalls    (1) Confusing the .union() method with the | operator, which requires both operands to be sets.  (2) Assuming the input lists contain unique values, which would make the set conversion redundant but harmless.  (3) Neglecting that the .union() method returns a new set, requiring an additional call to len() to obtain the final count.
# ──────────────────────────────────────────────────

# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
N = set(map(int,input().split()))
m =int(input())
M = set(map(int,input().split()))
print(len(list(N.union(M))))
