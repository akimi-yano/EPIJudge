from typing import List

from test_framework import generic_test

# This solution works !
# def intersect_two_sorted_arrays(A: List[int], B: List[int]) -> List[int]:
#     B_set = set(B)
#     ans = []
#     for num in A:
#         if num in B_set:
#             B_set.remove(num)
#             ans.append(num)
#     return ans

# This solution works !
def intersect_two_sorted_arrays(A: List[int], B: List[int]) -> List[int]:
    ans = []
    a = b = 0
    while a < len(A) and b < len(B):
        if A[a] < B[b]:
            a += 1
        elif A[a] > B[b]:
            b += 1
        else:
            if not ans or A[a] != ans[-1]:
                ans.append(A[a])
            a += 1
            b += 1
    return ans

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('intersect_sorted_arrays.py',
                                       'intersect_sorted_arrays.tsv',
                                       intersect_two_sorted_arrays))
