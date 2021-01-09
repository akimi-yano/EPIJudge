from typing import List
from collections import deque

from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


def binary_tree_from_preorder_inorder(preorder: List[int],
                                      inorder: List[int]) -> BinaryTreeNode:

    if not preorder or not inorder:
        return None
    val_idx = {inorder[i]: i for i in range(len(inorder))}
    
    def helper(pre_arr, in_arr):
        if not in_arr:
            return None

        node = BinaryTreeNode(pre_arr.popleft())
        left_in = deque([])
        while val_idx[in_arr[0]] < val_idx[node.data]:
            left_in.append(in_arr.popleft())

        # pop current node
        in_arr.popleft()
        
        right_in = in_arr

        node.left = helper(pre_arr, left_in)
        node.right = helper(pre_arr, right_in)
        return node
    
    return helper(deque(preorder), deque(inorder))
   
        
    
    
    return 


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('tree_from_preorder_inorder.py',
                                       'tree_from_preorder_inorder.tsv',
                                       binary_tree_from_preorder_inorder))
