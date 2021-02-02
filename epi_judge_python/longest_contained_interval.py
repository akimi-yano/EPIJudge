from typing import List

from test_framework import generic_test

# This solution works  - optimization
def longest_contained_range(A: List[int]) -> int:
    s = set(A)
    best = 0
    while s:
        left = right = s.pop()
        while left-1 in s:
            left -= 1
            s.remove(left)
        while right+1 in s:
            right += 1
            s.remove(right)
        best = max(best, right-left+1)
    return best

# This solution works
# def longest_contained_range(A: List[int]) -> int:
#     A.sort()
#     best  = 0
#     start = 0
#     subtraction =  0
#     if len(A) <= 1:
#         return len(A)
    
#     for i in range(1, len(A)):
#         if  A[i-1] == A[i]:
#             subtraction+=1
#         elif  A[i-1] +1 != A[i]:
#             start =  i
#             subtraction = 0
        
#         best = max(best, i-start+1-subtraction)
#     return best


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('longest_contained_interval.py',
                                       'longest_contained_interval.tsv',
                                       longest_contained_range))
