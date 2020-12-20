from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


# This solution works !

# def is_binary_tree_bst(tree: BinaryTreeNode) -> bool:
#     def helper(cur, lowerbound, upperbound):
#         if not cur:
#             return True
#         # if not lowerbound <= cur.data<= upperbound:
#         #     return False
#         if helper(cur.left, lowerbound, cur.data):
#             if lowerbound <= cur.data<= upperbound:
#                 if helper(cur.right, cur.data, upperbound):
#                     return True
#         return False        
#     return helper(tree, float('-inf'), float('inf'))

# it doesn't matter whether I do preorder check or inorder check - both works ! 

    #     3
    #   2   4
    # 1       5

# This solution works ! optimization 1 liner code

def is_binary_tree_bst(tree: BinaryTreeNode) -> bool:
    def helper(cur, lowerbound, upperbound):
        if not cur:
            return True
        if helper(cur.left, lowerbound, cur.data) and lowerbound <= cur.data<= upperbound and helper(cur.right, cur.data, upperbound):
            return True
        return False        
    return helper(tree, float('-inf'), float('inf'))

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_tree_a_bst.py', 'is_tree_a_bst.tsv',
                                       is_binary_tree_bst))
