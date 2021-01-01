from typing import List

from bst_node import BstNode
from test_framework import generic_test, test_utils

# This solution works 
# def find_k_largest_in_bst(tree: BstNode, k: int) -> List[int]:
#     def helper(cur):
#         if not cur:
#             return
#         helper(cur.left)
#         ans.append(cur.data)
#         helper(cur.right)      
    
#     ans = []
#     helper(tree)
#     return list(reversed(ans))[:k]

# This solution works
def find_k_largest_in_bst(tree: BstNode, k: int) -> List[int]:
    def helper(cur):
        nonlocal k 
        if not cur:
            return 
        if k == 0:
            return 
        helper(cur.right)
        if k > 0:
            ans.append(cur.data)
            k -= 1
            helper(cur.left)
    ans = []
    helper(tree)
    return ans
                

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('k_largest_values_in_bst.py',
                                       'k_largest_values_in_bst.tsv',
                                       find_k_largest_in_bst,
                                       test_utils.unordered_compare))
