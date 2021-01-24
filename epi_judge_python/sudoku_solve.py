import copy
import functools
import math
from typing import List

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

# This solution works:

def solve_sudoku(partial_assignment: List[List[int]]) -> bool:
    missing = []
    for r in range(9):
        for c in range(9):
            if not partial_assignment[r][c]:
                missing.append((r, c))
    
    def get_choices(r, c):
        choices = set([i for i in range(1,10)])
        for elem in partial_assignment[r]:
            if elem in choices:
                choices.remove(elem)
                
        for row in partial_assignment:
            if row[c] in choices:
                choices.remove(row[c])
                
        start_row = (r // 3) * 3
        start_col = (c // 3) * 3
        for row in range(start_row, start_row+3):
            for col in range(start_col, start_col+3):
                if partial_assignment[row][col] in choices:
                    choices.remove(partial_assignment[row][col])
        return choices

    def helper(idx):
        if idx >= len(missing):
            return True
        r, c = missing[idx]
        choices = get_choices(r,c)
        for choice in choices:
            partial_assignment[r][c] = choice
            if helper(idx+1):
                return True
        partial_assignment[r][c] = 0
        return False
    return helper(0)
    
    
    
    # This approach does not work:
    
    # def solve_sudoku(partial_assignment: List[List[int]]) -> bool:
    # ROW = len(partial_assignment)
    # COL = len(partial_assignment[0])

    # def isvalid():
    #     for row in range(ROW):
    #         seen = set([])
    #         for col in range(COL):
    #             if partial_assignment[row][col] in seen:
    #                 return False
    #             seen.add(partial_assignment[row][col])
                
    #     for col in range(COL):
    #         seen = set([])
    #         for row in range(ROW):
    #             if partial_assignment[row][col] in seen:
    #                 return False
    #             seen.add(partial_assignment[row][col])
                
    #     for start_row in range(0, ROW, 3):
    #         for start_col in range(0, COL, 3):
    #             seen = set([])
    #             for row in range(start_row, start_row+3):
    #                 for col in range(start_col, start_col+3):
    #                     if partial_assignment[row][col] in seen:
    #                         return False
    #                     seen.add(partial_assignment[row][col])
        
    #     return True
    
    # def helper(row, col):
    #     if not (0 <= row <= ROW-1) or not (0 <= col <= COL-1):
    #         return True
    #     if row == ROW-1 and col == COL-1 and isvalid():
    #         return True
    #     if partial_assignment[row][col] == 0:
    #         for i in range(1, 10):
    #             partial_assignment[row][col] = i
    #             if helper(row+1, col) | helper(row-1, col) | helper(row, col+1) | helper(row, col-1):
    #                 break
    #             else:
    #                 partial_assignment[row][col] = 0
    #         else:
    #             return False
    #     return True
    # return helper(0, 0)


def assert_unique_seq(seq):
    seen = set()
    for x in seq:
        if x == 0:
            raise TestFailure('Cell left uninitialized')
        if x < 0 or x > len(seq):
            raise TestFailure('Cell value out of range')
        if x in seen:
            raise TestFailure('Duplicate value in section')
        seen.add(x)


def gather_square_block(data, block_size, n):
    block_x = (n % block_size) * block_size
    block_y = (n // block_size) * block_size

    return [
        data[block_x + i][block_y + j] for j in range(block_size)
        for i in range(block_size)
    ]


@enable_executor_hook
def solve_sudoku_wrapper(executor, partial_assignment):
    solved = copy.deepcopy(partial_assignment)

    executor.run(functools.partial(solve_sudoku, solved))

    if len(partial_assignment) != len(solved):
        raise TestFailure('Initial cell assignment has been changed')

    for (br, sr) in zip(partial_assignment, solved):
        if len(br) != len(sr):
            raise TestFailure('Initial cell assignment has been changed')
        for (bcell, scell) in zip(br, sr):
            if bcell != 0 and bcell != scell:
                raise TestFailure('Initial cell assignment has been changed')

    block_size = int(math.sqrt(len(solved)))
    for i, solved_row in enumerate(solved):
        assert_unique_seq(solved_row)
        assert_unique_seq([row[i] for row in solved])
        assert_unique_seq(gather_square_block(solved, block_size, i))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('sudoku_solve.py', 'sudoku_solve.tsv',
                                       solve_sudoku_wrapper))
