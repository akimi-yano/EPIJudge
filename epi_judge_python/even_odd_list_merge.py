from typing import Optional

from list_node import ListNode
from test_framework import generic_test


# This solution works
def even_odd_merge(L: ListNode) -> Optional[ListNode]:
    '''
    cur/ L
     0   1   2   3   4
    [0] [1] [2] [3] [4]
                        cur
        
    even/ head1 
    [None] [0] [2] [4]
                   even
           
    odd/ head2 
    [None] [1] [3]
               odd
    '''
    cur = L
    even = head1 = ListNode(None)
    odd = head2 = ListNode(None)
    while cur:
        even.next = cur
        even = even.next
        cur = cur.next
        if cur:
            odd.next = cur
            odd = odd.next
            cur = cur.next
    even.next = head2.next
    # IMPORTANT! set the odd.next to None (otherwise it says connected to the even end)
    odd.next = None
    return head1.next
        

    
    
    return None


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('even_odd_list_merge.py',
                                       'even_odd_list_merge.tsv',
                                       even_odd_merge))
