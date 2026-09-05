# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/whats-your-name/problem?isFullScreen=true
# Problem     What's Your Name?
# Difficulty  Easy
# Subdomain   Strings
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-06-14, 02:52 p.m.
# Technique   f-string-interpolation
# Time        O(N+M)
# Space       O(N+M)
# Insight     The function utilizes Python f-string formatting to concatenate the provided first and last name strings into the required output template.
# Interview   Before: "How do I combine strings with specific formatting?" After: "I used an f-string to interpolate the variables directly into the template, resulting in O(N+M) time complexity where N and M are the lengths of the input strings."
# Pitfalls    (1) Failing to include the required exclamation mark after the last name as specified in the output format.  (2) Omitting the mandatory period at the end of the sentence.  (3) Adding extra spaces or missing the single space between the first and last name.
# ──────────────────────────────────────────────────

#
# Complete the 'print_full_name' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING first
#  2. STRING last
#

def print_full_name(first, last):
    # Write your code here
    print (f"Hello {first} {last}! You just delved into python.")

