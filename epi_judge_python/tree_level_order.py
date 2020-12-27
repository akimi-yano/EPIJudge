from typing import List

from binary_tree_node import BinaryTreeNode
from test_framework import generic_test

from collections import deque
def binary_tree_depth_order(tree: BinaryTreeNode) -> List[List[int]]:
    if not tree:
        return []
    queue = deque([tree])
    ans = []
    while queue:
        new_queue = deque([])
        level = []
        while queue:
            node = queue.popleft()
            level.append(node.data)
            if node.left:
                new_queue.append(node.left)
            if node.right:
                new_queue.append(node.right)
        queue = new_queue 
        ans.append(level)
    return ans


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('tree_level_order.py',
                                       'tree_level_order.tsv',
                                       binary_tree_depth_order))
