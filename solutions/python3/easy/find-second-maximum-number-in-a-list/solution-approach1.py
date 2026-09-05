# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem?isFullScreen=true
# Problem     Find the Runner-Up Score!  
# Difficulty  Easy
# Subdomain   Basic Data Types
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-06-14, 02:34 p.m.
# Technique   set-deduplication-and-sorting
# Time        O(N log N)
# Space       O(N)
# Insight     The implementation removes duplicate scores using a set, sorts the unique values, and selects the second-to-last element to identify the runner-up.
# Interview   Before: "I could iterate through the list to track the max and second-max." After: "Using a set to deduplicate followed by sorting is concise, running in O(N log N) time, which efficiently handles the requirement to find the second-highest unique score regardless of input size."
# Pitfalls    (1) Failing to handle duplicate scores by using a list instead of a set would return the wrong value if the maximum score appears multiple times.  (2) Assuming the input list always contains at least two unique scores, which is required for the index [-2] to be valid.
# ──────────────────────────────────────────────────

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    print(sorted(set(arr))[-2])
    
