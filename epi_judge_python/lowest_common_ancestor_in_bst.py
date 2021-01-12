import functools
from typing import Optional

from bst_node import BstNode
from test_framework import generic_test
from test_framework.binary_tree_utils import must_find_node
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


# Input nodes are nonempty and the key at s is less than or equal to that at b.
def find_lca(tree: BstNode, s: BstNode, b: BstNode) -> Optional[BstNode]:
    def helper(cur, t1, t2):
        if cur is t1 or cur is t2:
            return cur
        if t1.data < cur.data < t2.data:
            return cur
        elif t2.data < cur.data:
            return helper(cur.left, t1, t2)
        else:
            return helper(cur.right, t1, t2)
            
    if not tree or not s or not b: 
        return None
    if s.data < b.data:
        return helper(tree, s, b)
    else:
        return helper(tree, b, s)

@enable_executor_hook
def lca_wrapper(executor, tree, s, b):
    result = executor.run(
        functools.partial(find_lca, tree, must_find_node(tree, s),
                          must_find_node(tree, b)))
    if result is None:
        raise TestFailure('Result can\'t be None')
    return result.data


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('lowest_common_ancestor_in_bst.py',
                                       'lowest_common_ancestor_in_bst.tsv',
                                       lca_wrapper))
