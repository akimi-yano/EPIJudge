from typing import List

from test_framework import generic_test


def matrix_in_spiral_order(square_matrix: List[List[int]]) -> List[int]:
    N  = len(square_matrix)
    ans = []
    max_row = max_col = N-1
    min_row = min_col = 0
    while len(ans) < N * N:
        for col in range(min_col, max_col+1):
            ans.append(square_matrix[min_row][col])
        min_row += 1
        
        for row in range(min_row, max_row+1):
            ans.append(square_matrix[row][max_col])
        max_col -= 1
        
        for col in range(max_col, min_col -1, -1):
            ans.append(square_matrix[max_row][col])
        max_row -= 1
        
        for row in range(max_row, min_row -1, -1):
            ans.append(square_matrix[row][min_col])
        min_col += 1
        
    return ans


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('spiral_ordering.py',
                                       'spiral_ordering.tsv',
                                       matrix_in_spiral_order))
