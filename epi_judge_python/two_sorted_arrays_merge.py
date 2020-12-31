from typing import List

from test_framework import generic_test


# this solution works but there is a better way
# def merge_two_sorted_arrays(A: List[int], m: int, B: List[int],
#                             n: int) -> None:
#     # m is # elem of A
#     # n is # elem of B 
#     # [1,2,5,7]  [3,4,6]
#     #      a    b
#     a = b = 0
#     while n and a < m:
#         if A[a] <= B[b]:
#             a += 1
#         else:
#             A[a], B[b] = B[b], A[a]
#             a +=1
#             B.sort()
#     while b < n:
#         A[a] = B[b]
#         a += 1
#         b +=1
    
#     return

# This solution works ! - optimization
def merge_two_sorted_arrays(A: List[int], m: int, B: List[int], n: int) -> None:
    write_idx = m+n-1
    a = m-1 
    b = n-1
    while a >= 0 and b >= 0:
        if A[a] < B[b]:
            A[write_idx] = B[b]
            b -= 1
        else:
            A[write_idx] = A[a]
            a -= 1
        write_idx -= 1
        
    while b >= 0:
        A[write_idx] = B[b]
        b -= 1
        write_idx -= 1

def merge_two_sorted_arrays_wrapper(A, m, B, n):
    merge_two_sorted_arrays(A, m, B, n)
    return A


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('two_sorted_arrays_merge.py',
                                       'two_sorted_arrays_merge.tsv',
                                       merge_two_sorted_arrays_wrapper))
