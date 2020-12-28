import functools
from typing import Optional

from binary_tree_with_parent_prototype import BinaryTreeNode
from test_framework import generic_test
from test_framework.binary_tree_utils import must_find_node
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

# This solution works ! Time: O(H) where H is the depth of tree & Space: O(H) H call stack 
# def lca(node0: BinaryTreeNode,
#         node1: BinaryTreeNode) -> Optional[BinaryTreeNode]:
#     def helper(cur):
#         if cur is None:
#             return
#         seen.add(cur)
#         helper(cur.parent)
    
#     def helper2(cur):
#         if cur is None:
#             return None
#         if cur in seen:
#             return cur
#         return helper2(cur.parent)
    
#     seen = set([])
#     helper(node0)
#     return helper2(node1)

def get_height(node):
    height = 0
    while node is not None:
        height += 1
        node = node.parent
    return height

def lca(node0: BinaryTreeNode, node1: BinaryTreeNode) -> Optional[BinaryTreeNode]:
    # get height for both nodes and match the height and keep moving both - use iterative approach only
    n0_height = get_height(node0)
    n1_height = get_height(node1)
    while n0_height > n1_height:
        node0 = node0.parent
        n0_height -= 1
    while n1_height > n0_height:
        node1 = node1.parent
        n1_height -= 1
    while node0 is not node1:
        node0 = node0.parent
        node1 = node1.parent
    return node0

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
        generic_test.generic_test_main('lowest_common_ancestor_with_parent.py',
                                       'lowest_common_ancestor.tsv',
                                       lca_wrapper))
