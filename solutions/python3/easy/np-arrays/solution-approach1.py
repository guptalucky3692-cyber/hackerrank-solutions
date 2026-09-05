# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/np-arrays/problem?isFullScreen=true
# Problem     Arrays
# Difficulty  Easy
# Subdomain   Numpy
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-06-20, 01:47 p.m.
# Technique   numpy-array-slicing
# Time        O(N)
# Space       O(N)
# Insight     The implementation converts the input list into a NumPy array of floats and utilizes Python's slice notation to reverse the order of elements.
# Interview   Before: "How would you reverse a list and convert it to float types using NumPy?" After: "I use numpy.array with the float type argument, then apply the [::-1] slice operator. This approach runs in O(N) time and space, effectively handling the input array transformation."
# Pitfalls    (1) Failing to specify the float type in numpy.array results in default integer types if the input contains only integers.  (2) Using incorrect slice syntax like [:-1] instead of [::-1] will omit the first element of the array.
# ──────────────────────────────────────────────────



def arrays(arr):
    # complete this function
    # use numpy.array
    arr = numpy.array(arr,float)
    return arr[::-1]
