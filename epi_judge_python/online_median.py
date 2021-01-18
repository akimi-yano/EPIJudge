from typing import Iterator, List
import heapq

from test_framework import generic_test

# 1, 0, 3, 5, 2, 0, 1
# maxheap: [1]
# minheap: []
def balance_heaps(maxheap, minheap):
    while len(maxheap) > len(minheap) + 1:
        elem = -heapq.heappop(maxheap)
        heapq.heappush(minheap, elem)
    if len(minheap) < 1:
        return
    while -maxheap[0] > minheap[0]:
        m1 = -heapq.heappop(maxheap)
        m2 = heapq.heappop(minheap)
        heapq.heappush(maxheap, -m2)
        heapq.heappush(minheap, m1)

def online_median(sequence: Iterator[int]) -> List[float]:
    ans = []
    minheap = []
    maxheap = []
    for num in sequence:
        heapq.heappush(maxheap, -num)
        balance_heaps(maxheap, minheap)
        if len(maxheap) > len(minheap):
            median = -maxheap[0]
            ans.append(median)
        else:
            m1 = -maxheap[0]
            m2 = minheap[0]
            ans.append((m1+m2) / 2)
    return ans


def online_median_wrapper(sequence):
    return online_median(iter(sequence))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('online_median.py', 'online_median.tsv',
                                       online_median_wrapper))
