import functools
from typing import List, Optional

from bst_node import BstNode
from test_framework import generic_test
from test_framework.binary_tree_utils import (binary_tree_height,
                                              generate_inorder)
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

# This solution works ! - dont forget to do end + start // 2 (addition not subtraction)
# print to debug 

def build_min_height_bst_from_sorted_array(A: List[int]) -> Optional[BstNode]:
    def helper(start, end):
        if end - start < 0:
            return None
        mid_idx = (end+start)//2
        node = BstNode(A[mid_idx])
        node.left = helper(start, mid_idx-1)
        node.right = helper(mid_idx+1, end)
        return node
    
    if not A:
        return None
    return helper(0, len(A)-1)


@enable_executor_hook
def build_min_height_bst_from_sorted_array_wrapper(executor, A):
    result = executor.run(
        functools.partial(build_min_height_bst_from_sorted_array, A))

    if generate_inorder(result) != A:
        raise TestFailure('Result binary tree mismatches input array')
    return binary_tree_height(result)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'bst_from_sorted_array.py', 'bst_from_sorted_array.tsv',
            build_min_height_bst_from_sorted_array_wrapper))
