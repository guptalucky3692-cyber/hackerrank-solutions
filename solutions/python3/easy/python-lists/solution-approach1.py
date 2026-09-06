# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/python-lists/problem?isFullScreen=true
# Problem     Lists
# Difficulty  Easy
# Subdomain   Basic Data Types
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-09-06, 12:53 p.m.
# ──────────────────────────────────────────────────

if __name__ == '__main__':
    N = int(input())
    list =[]
    for i in range(N):
        command = input().lower().split()
        if command[0]=="insert":
            list.insert(int(command[1]), int(command[2]))
        elif command[0]=="remove":
            list.remove(int(command[1]))
        elif command[0]=="append":
            list.append(int(command[1]))
        elif command[0]=="sort":
            list.sort()
        elif command[0]=="pop":
            list.pop()
        elif command[0]=="reverse":
            list.reverse()
        elif command[0] == "print":
            print(list)
        else:
            print("Enter a valid command!")
    
