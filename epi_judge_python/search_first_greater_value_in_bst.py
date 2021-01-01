from typing import Optional

from bst_node import BstNode
from test_framework import generic_test


# This solution works 
# def find_first_greater_than_k(tree: BstNode, k: int) -> Optional[BstNode]:
#     def helper(cur, target):
#         nonlocal ans

#         if not cur:
#             return 
#         helper(cur.left, target)
#         if cur.data > target:
#             ans = min(ans, cur, key=lambda node: node.data) if ans is not None else cur
#             return
#         helper(cur.right, target)

#     ans = None
#     helper(tree, k)
#     return ans if ans else None

def find_first_greater_than_k(tree: BstNode, k: int) -> Optional[BstNode]:
    # definide this here before the helper definition
    smallest_node = None
    
    def helper(cur):
        nonlocal k, smallest_node
        if not cur:
            return 
        if cur.data > k:
            if (smallest_node is None) or (smallest_node and smallest_node.data > cur.data):
                smallest_node = cur
            helper(cur.left)
        else:
            helper(cur.right)
    
    helper(tree)
    return smallest_node

def find_first_greater_than_k_wrapper(tree, k):
    result = find_first_greater_than_k(tree, k)
    return result.data if result else -1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'search_first_greater_value_in_bst.py',
            'search_first_greater_value_in_bst.tsv',
            find_first_greater_than_k_wrapper))
