# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/exceptions/problem?isFullScreen=true
# Problem     Exceptions
# Difficulty  Easy
# Subdomain   Errors and Exceptions
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-07-02, 07:16 p.m.
# Technique   try-except-block-handling
# Time        O(T)
# Space       O(1)
# Insight     The implementation uses a try-except block to catch and print specific runtime exceptions during integer division operations.
# Pitfalls    (1) Failing to use integer division operator // as specified in the Python 3 requirements.  (2) Neglecting to catch both ZeroDivisionError and ValueError separately as required by the problem statement.  (3) Printing the error message without the required 'Error Code: ' prefix.
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
    
