from list_node import ListNode
from test_framework import generic_test


def is_linked_list_a_palindrome(L: ListNode) -> bool:
    # 1 2 3 2 1
    #         f
    #     s 
    #   p
    
    # 3 2 1
    #   p c n
    
    if not L:
        return True
    
    fast = slow = prev_slow = L
    while fast and fast.next:
        fast = fast.next.next
        prev_slow = slow
        slow = slow.next
    prev_slow.next = None
    
    prev =  None
    cur = slow
    while cur:
        nextnode = cur.next
        cur.next =  prev
        prev = cur
        cur = nextnode
    
    right = prev
    left = L
    while right and left:
        if right.data != left.data:
            return False
        right = right.next
        left = left.next
    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_list_palindromic.py',
                                       'is_list_palindromic.tsv',
                                       is_linked_list_a_palindrome))
