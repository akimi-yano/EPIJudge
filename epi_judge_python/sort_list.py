from typing import Optional

from list_node import ListNode
from test_framework import generic_test


def stable_sort_list(L: ListNode) -> Optional[ListNode]:
    # 5 -> 1 -> 3 -> 4 -> 2 -> x
    # 1 -> 2 -> 3 -> 4 -> 5 -> x
    '''
    merge sort to do stable sort
    '''
    def helper(cur):
        if not cur  or not cur.next:
            return cur

        prev_slow = None
        fast = slow = cur
        while fast and fast.next:
            fast = fast.next.next
            prev_slow = slow
            slow = slow.next
        lasthalf = prev_slow.next
        prev_slow.next = None

        first = helper(cur)
        second = helper(lasthalf)
        
        cur1 = first
        cur2 = second
        if cur1 is None:
            return cur2
        if cur2 is None:
            return cur1

        newcur = dummyhead = ListNode(None)

        while cur1 and cur2:
            if cur1.data < cur2.data:
                newcur.next = cur1
                newcur = newcur.next
                cur1 = cur1.next
                newcur.next = None
            else:
                newcur.next = cur2
                newcur = newcur.next
                cur2 = cur2.next
                newcur.next = None
        if cur1:
            newcur.next = cur1
        if cur2:
            newcur.next = cur2
        return dummyhead.next
    return helper(L)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('sort_list.py', 'sort_list.tsv',
                                       stable_sort_list))
