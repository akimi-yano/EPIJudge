import functools

from list_node import ListNode
from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


# def overlapping_no_cycle_lists(l0: ListNode, l1: ListNode) -> ListNode:
#     seen = set()
#     cur1 = l0
#     while cur1:
#         seen.add(cur1.data)
#         cur1 = cur1.next
#     cur2 = l1
#     while cur2:
#         if cur2.data in seen:
#             return cur2
#         seen.add(cur2.data)
#         cur2 = cur2.next
#     return None


# Time: O(M+N)
# Space: O(1)
'''
it works because after iterating m+n(+k) nodes, they should meet
'''
def overlapping_no_cycle_lists(l0: ListNode, l1: ListNode) -> ListNode:
    cur1 = l0 
    cur2 = l1
    while True:
        if cur1 == cur2:
            return cur1
        cur1 = cur1.next if cur1 else l1
        cur2 = cur2.next if cur2 else l0


@enable_executor_hook
def overlapping_no_cycle_lists_wrapper(executor, l0, l1, common):
    if common:
        if l0:
            i = l0
            while i.next:
                i = i.next
            i.next = common
        else:
            l0 = common

        if l1:
            i = l1
            while i.next:
                i = i.next
            i.next = common
        else:
            l1 = common

    result = executor.run(functools.partial(overlapping_no_cycle_lists, l0,
                                            l1))

    if result != common:
        raise TestFailure('Invalid result')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('do_terminated_lists_overlap.py',
                                       'do_terminated_lists_overlap.tsv',
                                       overlapping_no_cycle_lists_wrapper))
