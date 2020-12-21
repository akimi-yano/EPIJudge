import functools
from typing import List

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

NUM_PEGS = 3


def compute_tower_hanoi(num_rings: int) -> List[List[int]]:
    ans = []
    def helper(n, from_pole, to_pole, other_pole):
        if n == 1:
            # just move it to the destination
            ans.append([from_pole, to_pole])
        else:
            # 1 move the top ones (n-1) to the other pole
            helper(n-1, from_pole, other_pole, to_pole)
            # 2 move the bottom one to the destination 
            ans.append([from_pole, to_pole])
            # 3 move the top ones to the destination 
            helper(n-1, other_pole, to_pole, from_pole)
    helper(num_rings, 0, 1, 2)
    return ans
    
    
    # P0         P1         P2
    # -         
    # --
    # ---
    # ----
    # -----
    # ------
    
    # P0          P1         P2
                # -         
                # --
                # ---
                # ----
                # -----
                # ------  

    # if n == 1:
    #     return [[0,1]]
    # if n == 2:
    #     return [[0,2],[0,1],[2,1]]
    # if n == 3:
    #     return [[0,1],[0,2],[1,2],[0,1],[2,0],[2,1],[0,1]]


























@enable_executor_hook
def compute_tower_hanoi_wrapper(executor, num_rings):
    pegs = [list(reversed(range(1, num_rings + 1)))
            ] + [[] for _ in range(1, NUM_PEGS)]

    result = executor.run(functools.partial(compute_tower_hanoi, num_rings))

    for from_peg, to_peg in result:
        if pegs[to_peg] and pegs[from_peg][-1] >= pegs[to_peg][-1]:
            raise TestFailure('Illegal move from {} to {}'.format(
                pegs[from_peg][-1], pegs[to_peg][-1]))
        pegs[to_peg].append(pegs[from_peg].pop())
    expected_pegs1 = [[], [], list(reversed(range(1, num_rings + 1)))]
    expected_pegs2 = [[], list(reversed(range(1, num_rings + 1))), []]
    if pegs not in (expected_pegs1, expected_pegs2):
        raise TestFailure('Pegs doesn\'t place in the right configuration')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('hanoi.py', 'hanoi.tsv',
                                       compute_tower_hanoi_wrapper))
