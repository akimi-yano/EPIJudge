from typing import List

from test_framework import generic_test


# Check if a partially filled matrix has any conflicts.
def is_valid_sudoku(partial_assignment: List[List[int]]) -> bool:
    # [[0,0,0,0,0,0,0,0,0],
    #  [0,0,0,0,0,0,0,0,0],
    #  [0,0,0,0,0,0,0,0,0],
    #  [0,0,0,0,0,0,0,0,0],
    #  [0,0,0,0,0,0,0,0,0],
    #  [0,0,0,0,0,0,0,0,0],
    #  [0,0,0,0,0,0,0,0,0],
    #  [0,0,0,0,0,0,0,0,0],
    #  [0,0,0,0,0,0,0,0,0]]
    # check each row, col, 3X3 to see if there is any duplicate (outside of 0)
    
    return are_rows_valid(partial_assignment) and are_cols_valid(partial_assignment) and are_3x3_valid(partial_assignment)

def are_rows_valid(partial_assignment):
    for row in partial_assignment:
        seen = set([])
        for val in row:
            if val != 0 and val in seen:
                return False
            seen.add(val)
    return True

def are_cols_valid(partial_assignment):
    for col in range(len(partial_assignment[0])):
        seen = set([])
        for row in range(len(partial_assignment)):
            val = partial_assignment[row][col] 
            if val != 0 and val in seen:
                return False
            seen.add(val)
    return True

def are_3x3_valid(partial_assignment):
    for start_row in range(0,len(partial_assignment),3):
        for start_col in range(0,len(partial_assignment),3):
            seen = set([])
            for row in range(3):
                for col in range(3):
                    val = partial_assignment[start_row + row][start_col + col]
                    if val != 0 and val in seen:
                        return False
                    seen.add(val)
    return True
                
if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_valid_sudoku.py',
                                       'is_valid_sudoku.tsv', is_valid_sudoku))
