from typing import List, Optional

from bst_node import BstNode
from test_framework import generic_test

# this solution works - important to make the nonlocal variable for idx (dont pass in the recursion)
# its because the array index should change by using each element and move (not in the recurion but iteration)  
def rebuild_bst_from_preorder(preorder_sequence: List[int]) -> Optional[BstNode]:
    if not preorder_sequence:
        return None

    idx = 0
    arr = preorder_sequence
    
    def helper(left_limit, right_limit):
        nonlocal idx
        nonlocal arr
        if idx >= len(arr) or not left_limit < arr[idx] < right_limit:
            return None

        node = BstNode(data=arr[idx])
        idx += 1
        
        node.left = helper(left_limit, node.data)
        node.right = helper(node.data, right_limit)
        return node

    root = helper(float('-inf'), float('inf'))

    return root



if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('bst_from_preorder.py',
                                       'bst_from_preorder.tsv',
                                       rebuild_bst_from_preorder))
