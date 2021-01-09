from typing import Iterator, List

from test_framework import generic_test


# Time: O(NlogK)
# Space: O(N)
    
import heapq
def sort_approximately_sorted_array(sequence: Iterator[int],
                                    k: int) -> List[int]:
    minheap = []
    ans = []
    for elem in sequence:
        heapq.heappush(minheap, elem)
        if len(minheap) > k:
            ans.append((heapq.heappop(minheap)))
    while minheap:
        ans.append((heapq.heappop(minheap)))
    return ans


def sort_approximately_sorted_array_wrapper(sequence, k):
    return sort_approximately_sorted_array(iter(sequence), k)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'sort_almost_sorted_array.py', 'sort_almost_sorted_array.tsv',
            sort_approximately_sorted_array_wrapper))
