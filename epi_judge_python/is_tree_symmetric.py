from binary_tree_node import BinaryTreeNode
from test_framework import generic_test

# This solution works
def helper(left, right):
    if not left or not right:
        return left is right

    return helper(left.left, right.right) and left.data == right.data and helper(left.right, right.left)
    
def is_symmetric(tree: BinaryTreeNode) -> bool:
    if not tree:
        return True
    return helper(tree.left, tree.right)

# This solution works 
# from collections import deque
# def is_symmetric(tree: BinaryTreeNode) -> bool:
#     if not tree:
#         return True
#     queue = deque([tree])
#     while queue:
#         new_queue = deque([])
#         while queue:
#             node = queue.popleft()
#             if node:
#                 new_queue.append(node.left)
#                 new_queue.append(node.right)
#         queue = deque(new_queue)
#         while new_queue:
#             left = new_queue.popleft()
#             right = new_queue.pop()
#             if (not left and right) or (left and not right) or ((left and right) and (left.data != right.data)):
#                 return False
#     return True
    
# # This solution works !
# def is_symmetric(tree: BinaryTreeNode) -> bool:  
#     def helper(cur1, cur2):
#         if not cur1:
#             if cur2:
#                 return False
#             else:
#                 return True
#         elif not cur2:
#             return False
#         elif cur1.data != cur2.data:
#             return False
#         else:
#             cur1.data == cur2.data
#             opt1 = helper(cur1.left, cur2.right)
#             opt2 = helper(cur1.right, cur2.left)
#             return opt1 and opt2
#     if not tree:
#         return True
#     return helper(tree.left, tree.right)

# [0, -13, -13, 1, null, null, 1, null, 91, 91, null, 99, 78, 78, 99, null, -91, null, -64, -64, null, -91]
    #           [0, 
    #    -13,       -13, 
    #  1,   null,   null, 1, 
#  null,91, 91,null, 99,78, 78,99, 
#       null,-91, null, -64, -64, null, -91]
if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_tree_symmetric.py',
                                       'is_tree_symmetric.tsv', is_symmetric))
