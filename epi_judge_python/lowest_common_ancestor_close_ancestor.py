import functools
from typing import Optional

from binary_tree_with_parent_prototype import BinaryTreeNode
from test_framework import generic_test
from test_framework.binary_tree_utils import must_find_node
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


# This solution works!:
def lca(node0: BinaryTreeNode,
        node1: BinaryTreeNode) -> Optional[BinaryTreeNode]:
    cur1, cur2 = node0, node1
    if cur1 is cur2:
        return cur1
    seen = set([])
    while cur1.parent and cur2.parent:
        if cur1 in seen:
            return cur1
        seen.add(cur1)
        cur1 = cur1.parent
        
        if cur2 in seen:
            return cur2
        seen.add(cur2)
        cur2 = cur2.parent
    
    while cur1.parent:
        if cur1 in seen:
            return cur1
        seen.add(cur1)
        cur1 = cur1.parent

    while cur2.parent:
        if cur2 in seen:
            return cur2
        seen.add(cur2)
        cur2 = cur2.parent
    
    return cur1
        
@enable_executor_hook
def lca_wrapper(executor, tree, node0, node1):
    result = executor.run(
        functools.partial(lca, must_find_node(tree, node0),
                          must_find_node(tree, node1)))

    if result is None:
        raise TestFailure('Result can\'t be None')
    return result.data


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'lowest_common_ancestor_close_ancestor.py',
            'lowest_common_ancestor.tsv', lca_wrapper))
