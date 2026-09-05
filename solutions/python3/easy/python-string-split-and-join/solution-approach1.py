# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/python-string-split-and-join/problem?isFullScreen=true
# Problem     String Split and Join
# Difficulty  Easy
# Subdomain   Strings
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-06-20, 05:03 p.m.
# Technique   split-join-string-transformation
# Time        O(n)
# Space       O(n)
# Insight     The implementation utilizes Python's built-in string methods to tokenize the input by whitespace and reconstruct it using a hyphen delimiter.
# Interview   Before: "How would you replace spaces with hyphens in a string?" After: "I would use the split and join methods, which operate in O(n) time and space, to efficiently transform the string by splitting on whitespace and joining with the hyphen character."
# Pitfalls    (1) Using split() without arguments handles multiple spaces differently than split(' '), which may lead to unexpected results if the input contains consecutive spaces.  (2) The join method must be called on the delimiter string, not the list of words.
# ──────────────────────────────────────────────────

def split_and_join(line):
    # write your code here
    line = line.split()
    return "-".join(line)
