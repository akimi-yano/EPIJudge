from typing import Optional

from list_node import ListNode
from test_framework import generic_test


# this solution works !
    # 1 -> 2 -> 3 -> 4 -> 5
        # *   *   *
    # 1 -> 4 -> 3 -> 2 -> 5
    # 1 - 2 - 3 - 4 - 5
        # *   *   *
def reverse_sublist(L: ListNode, start: int,
                    finish: int) -> Optional[ListNode]:
    if not L:
        return None
    if start == finish:
        return L
    head = cur = L
    idx = 1

    before_node = None
    start_node = head
    for i in range(start - 1):
        if not before_node:
            before_node = head
        else:
            before_node = before_node.next
        start_node = start_node.next
    
    after_node = start_node.next
    for i in range(start, finish):
        after_node = after_node.next
    
    def reverse(before_node, start_node, after_node, head):
        prev = after_node
        cur = start_node 
        while cur != after_node:
            next_node = cur.next
            cur.next = prev
            prev = cur
            cur =  next_node
            
        if  before_node:
            before_node.next = prev
        else:
            head = prev

        return head
        
    
    return reverse(before_node, start_node, after_node, head)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('reverse_sublist.py',
                                       'reverse_sublist.tsv', reverse_sublist))
