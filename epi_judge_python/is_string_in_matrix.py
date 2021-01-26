from typing import List

from test_framework import generic_test

from functools import lru_cache
def is_pattern_contained_in_grid(grid: List[List[int]], pattern: List[int]) -> bool:
    
    @lru_cache(None)
    def helper(row, col, i):
        if i > len(pattern)-1:
            return True
        if not (0 <= row <= ROW-1) or not (0 <= col <= COL-1):
            return False
        if grid[row][col] == pattern[i]:
            return helper(row+1, col, i+1) | helper(row-1, col, i+1) | helper(row, col+1, i+1) | helper(row, col-1, i+1)
        return False
    
    if not pattern or not grid:
        return False
    ROW = len(grid)
    COL = len(grid[0])
    for row in range(ROW):
        for col in range(COL):
            if grid[row][col] == pattern[0]:
                if helper(row, col, 0):
                    return True
    return False
    


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_string_in_matrix.py',
                                       'is_string_in_matrix.tsv',
                                       is_pattern_contained_in_grid))
