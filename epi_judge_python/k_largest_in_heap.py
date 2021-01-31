from typing import List

from test_framework import generic_test, test_utils


import heapq
def k_largest_in_binary_heap(A: List[int], k: int) -> List[int]:
    if not A or not k:
        return []

    maxheap = [(-A[0],0)]
    ans = []
    while len(ans) < k:
        num, idx = heapq.heappop(maxheap)
        ans.append(-num)
        left_child, right_child = idx*2+1, idx*2+2
        if left_child < len(A):
            heapq.heappush(maxheap, (-A[left_child], left_child))
        if right_child < len(A):
            heapq.heappush(maxheap, (-A[right_child], right_child))
    return ans


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'k_largest_in_heap.py',
            'k_largest_in_heap.tsv',
            k_largest_in_binary_heap,
            comparator=test_utils.unordered_compare))
