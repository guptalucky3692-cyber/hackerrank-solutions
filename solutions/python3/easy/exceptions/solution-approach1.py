# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/exceptions/problem?isFullScreen=true
# Problem     Exceptions
# Difficulty  Easy
# Subdomain   Errors and Exceptions
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-07-02, 07:16 p.m.
# ──────────────────────────────────────────────────

# Enter your code here. Read input from STDIN. Print output to STDOUT           
if __name__ == "__main__":
    t = int(input())
    
    for _ in range(t):
        a, b = input().split()
        
        try:
            print(int(a)//int(b))
        except ZeroDivisionError:
            print("Error Code: integer division or modulo by zero")
        except ValueError as e:
            print("Error Code:",e)
    
