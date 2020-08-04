from binary_tree_node import BinaryTreeNode
from test_framework import generic_test
import collections

# def is_balanced_binary_tree(tree: BinaryTreeNode) -> bool:
#     def helper(cur):
#         if not cur:
#             return 0
#         left = helper(cur.left)
#         right = helper(cur.right)
#         if abs(left-right)<=1:
#             return 1 + max(left,right) 
#         return float('inf')
#     return helper(tree) !=float('inf')

def is_balanced_binary_tree(tree: BinaryTreeNode) -> bool:
    BalancedStatusWithHeight = collections.namedtuple(
        'BalancedStatusWithHeight',('balanced','height'))
    # First value of the return value indicates if tree is balanced, and if 
    # balanced the second value of the return valie is the height of tree.
    def check_balanced(tree):
        if not tree:
            return BalancedStatusWithHeight(balanced=True, height=-1)
        left_result = check_balanced(tree.left)
        if not left_result.balanced:
            return left_result
        right_result = check_balanced(tree.right)
        if not right_result.balanced:
            return right_result

        is_balanced= abs(left_result.height-right_result.height) <= 1
        height = max(left_result.height,right_result.height)+1
        return BalancedStatusWithHeight(is_balanced,height)
    return check_balanced(tree).balanced


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_tree_balanced.py',
                                       'is_tree_balanced.tsv',
                                       is_balanced_binary_tree))
