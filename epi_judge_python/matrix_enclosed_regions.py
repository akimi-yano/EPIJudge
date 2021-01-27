from typing import List

from test_framework import generic_test

# This solution works - dont traverse using recursion if I am just gonna check each element and change it into something else
def fill_surrounded_regions(board: List[List[str]]) -> None:
    ROW = len(board)
    COL = len(board[0])
    
    def helper(row, col):
        if not (0<=row<=ROW-1) or not(0<=col<=COL-1) or board[row][col] != 'W':
            return
        board[row][col] = 'T'
        helper(row, col+1)
        helper(row, col-1)
        helper(row+1, col)
        helper(row-1, col)
    
    for row in range(ROW):
        if board[row][0] == 'W':
            helper(row, 0)
        if board[row][COL-1] == 'W':
            helper(row, COL-1)
            
    for col in range(COL):
        if board[0][col] == 'W':
            helper(0, col)
        if board[ROW-1][col] == 'W':
            helper(ROW-1, col)
            
    for row in range(ROW):
        for col in range(COL):
            if board[row][col] == 'W':
                board[row][col] = 'B'
                # helper(row, col, 'W', 'B') -  no need
            
    for row in range(ROW):
        for col in range(COL):
            if board[row][col] == 'T':
                board[row][col] = 'W'
                # helper(row, col, 'T', 'W') - no need



def fill_surrounded_regions_wrapper(board):
    fill_surrounded_regions(board)
    return board


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('matrix_enclosed_regions.py',
                                       'matrix_enclosed_regions.tsv',
                                       fill_surrounded_regions_wrapper))
