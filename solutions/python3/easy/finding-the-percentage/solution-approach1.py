# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/finding-the-percentage/problem?isFullScreen=true
# Problem     Finding the percentage
# Difficulty  Easy
# Subdomain   Basic Data Types
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-07-02, 07:45 p.m.
# Technique   hash-map-lookup
# Time        O(N + M)
# Space       O(N * M)
# Insight     The implementation maps student names to lists of floating-point scores and computes the arithmetic mean of the target student's marks using the sum and length functions.
# Interview   Before: "I would iterate through the list and check each name." After: "Using a dictionary provides O(1) average lookup time for the query_name, resulting in O(N + M) total time complexity where N is the number of students and M is the number of marks per student."
# Pitfalls    (1) Failing to format the output to exactly two decimal places using the f-string specifier .2f.  (2) Assuming the input marks are integers when the problem requires floating-point precision.  (3) Neglecting to handle the case where the query_name might not exist in the dictionary.
# ──────────────────────────────────────────────────

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
for name in student_marks:
    if query_name == name:
        avg = sum(student_marks[name])/len(student_marks[name])
print(f"{avg:.2f}")
