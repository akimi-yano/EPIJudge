import functools
from typing import List

from binary_tree_node import BinaryTreeNode
from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook

# This solution works:
def reconstruct_preorder(preorder: List[int]) -> BinaryTreeNode:
    if not preorder:
        return None

    def helper():
        nonlocal i
        data = preorder[i]
        i += 1
        if data is None:
            return  None
        node = BinaryTreeNode(data)
        node.left = helper()
        node.right  = helper()
        return node
    
    i = 0
    return helper()
    
            

# This solution works:
# def reconstruct_preorder(preorder: List[int]) -> BinaryTreeNode:
    
#     def helper(cur):
#         nonlocal i
#         i += 1
#         if cur.data is None:
#             return None
#         cur.left = helper(BinaryTreeNode(preorder[i]))
#         cur.right = helper(BinaryTreeNode(preorder[i]))
#         return cur
#     i = 0
#     return helper(BinaryTreeNode(preorder[i]))


@enable_executor_hook
def reconstruct_preorder_wrapper(executor, data):
    data = [None if x == 'null' else int(x) for x in data]
    return executor.run(functools.partial(reconstruct_preorder, data))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('tree_from_preorder_with_null.py',
                                       'tree_from_preorder_with_null.tsv',
                                       reconstruct_preorder_wrapper))
