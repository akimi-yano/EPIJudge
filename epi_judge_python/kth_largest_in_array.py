from typing import List

from test_framework import generic_test


# The numbering starts from one, i.e., if A = [3, 1, -1, 2]
# find_kth_largest(1, A) returns 3, find_kth_largest(2, A) returns 2,
# find_kth_largest(3, A) returns 1, and find_kth_largest(4, A) returns -1.
import heapq
def find_kth_largest(k: int, A: List[int]) -> int:
    minheap = []
    for num in A:
        heapq.heappush(minheap, num)
        if len(minheap) > k:
            heapq.heappop(minheap)
    return heapq.heappop(minheap)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('kth_largest_in_array.py',
                                       'kth_largest_in_array.tsv',
                                       find_kth_largest))
