# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/python-lists/problem?isFullScreen=true
# Problem     Lists
# Difficulty  Easy
# Subdomain   Basic Data Types
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-09-06, 12:53 p.m.
# Technique   command-pattern-list-dispatch
# Time        O(N * M) where N is the number of comma…
# Space       O(M) where M is the maximum number of e…
# Insight     The implementation maps string-based command inputs to corresponding Python list methods to dynamically manipulate the list state.
# Interview   Before: "I would use a series of if-else statements to handle each command." After: "I used a command-pattern approach to map inputs to list methods, resulting in O(N * M) time complexity, where M is the list size, as operations like insert and remove are O(M)."
# Pitfalls    (1) The remove method raises a ValueError if the specified integer is not present in the list.  (2) The insert method shifts elements, making it O(M) rather than O(1).  (3) The pop method raises an IndexError if called on an empty list.
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
    
