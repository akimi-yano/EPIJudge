from typing import List

from test_framework import generic_test


# TIME: O(N^2) 
# SPACE: O(N)

# This solution works 

# def has_three_sum(A: List[int], t: int) -> bool:
#     A_set = set(A)
#     for x in A:
#         for y in A:
#             if (t -(x + y)) in A_set:
#                 return True
#     return False


# takes sorted list as an input and target and returns boolean if there is two sum
def has_two_sum(A, t):
    i, j = 0, len(A)-1
    while i <= j:
        if A[i] + A[j] == t:
            return True 
        elif A[i] + A[j] < t:
            i += 1
        else:
            # A[i] + A[j] > t
            j -= 1
    return False

def has_three_sum(A, t):
    A.sort()
    # Finds if the sum of two numbers in A equals to t - a
    return any(has_two_sum(A, t-a) for a in A) 




if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('three_sum.py', 'three_sum.tsv',
                                       has_three_sum))
