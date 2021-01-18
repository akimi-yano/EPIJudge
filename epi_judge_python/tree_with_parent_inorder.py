from typing import List

from binary_tree_with_parent_prototype import BinaryTreeNode
from test_framework import generic_test

def inorder_traversal(tree: BinaryTreeNode) -> List[int]:
    if tree is None:
        return []

    ans = []
    prev, cur = tree.parent, tree
    while cur:
        # if previous node was the parent, we should go left.
        if prev == cur.parent:
            # if we can go left
            if cur.left is not None:
                prev, cur = cur, cur.left
            # if we cannot go left
            else:
                # add current node to answer
                ans.append(cur.data)
                # if we can go right
                if cur.right is not None:
                    prev, cur = cur, cur.right
                # if we cannot go right
                else:
                    # go to parent
                    prev, cur = cur, cur.parent
        # if previous node was the left, we should go right.
        elif prev == cur.left:
            # add current node to answer
            ans.append(cur.data)
            # if we can go right
            if cur.right is not None:
                prev, cur = cur, cur.right
            # if we cannot go right
            else:
                # go to parent
                prev, cur = cur, cur.parent
        # if previous node was the right, we should go to parent.
        else:
            # go to parent
            prev, cur = cur, cur.parent
    return ans


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('tree_with_parent_inorder.py',
                                       'tree_with_parent_inorder.tsv',
                                       inorder_traversal))
