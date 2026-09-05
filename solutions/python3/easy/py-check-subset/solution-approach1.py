# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/py-check-subset/problem?isFullScreen=true
# Problem     Check Subset
# Difficulty  Easy
# Subdomain   Sets
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-06-22, 02:23 p.m.
# Technique   set-issubset-method
# Time        O(N * (len(A) + len(B)))
# Space       O(len(A) + len(B))
# Insight     The implementation leverages the built-in set.issubset method to verify if every element of set A exists within set B.
# Interview   Before: "I would iterate through every element of A and check its existence in B using a loop." After: "Using the built-in issubset method is more idiomatic and efficient, operating in O(len(A) + len(B)) time complexity, which is optimal for set membership verification."
# Pitfalls    (1) Confusing the subset method with the proper subset operator, which requires strict inequality.  (2) Failing to handle the input format correctly by assuming the number of elements provided matches the actual count of space-separated integers.
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
    
