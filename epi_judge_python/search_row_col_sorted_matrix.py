from typing import List

from test_framework import generic_test

# This solution works - optimization:
def matrix_search(A: List[List[int]], x: int) -> bool:
    ROW = len(A)
    COL  = len(A[0])
    row = 0
    col = COL-1
    while 0<=row<ROW and 0<=col<COL:
        if A[row][col] == x:
            return True
        elif  A[row][col] > x:
            col -= 1
        else:
            row += 1
    return False

# This solution works:
# def matrix_search(A: List[List[int]], x: int) -> bool:
    
#     def binary_search(row):
#         nonlocal x
#         left = 0
#         right  =  COL -1
#         while left <=  right:
#             mid = (left + right) // 2
#             if  A[row][mid] == x:
#                 return True
#             elif  A[row][mid] > x:
#                 right = mid-1
#             else:
#                 left = mid+1
#         return False
        
#     ROW = len(A)
#     COL  = len(A[0])
#     for row in range(ROW):
#         if A[row][0] <= x <= A[row][COL-1]:
#             if binary_search(row):
#                 return True
#     return False


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('search_row_col_sorted_matrix.py',
                                       'search_row_col_sorted_matrix.tsv',
                                       matrix_search))
