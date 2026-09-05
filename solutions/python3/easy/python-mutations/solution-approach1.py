# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/python-mutations/problem?isFullScreen=true
# Problem     Mutations
# Difficulty  Easy
# Subdomain   Strings
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-06-20, 05:12 p.m.
# ──────────────────────────────────────────────────

def mutate_string(string, position, character):
    s = string[:position] + character +  string[position+1:]
    return s
