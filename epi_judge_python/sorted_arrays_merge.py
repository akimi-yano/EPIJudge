from typing import List

from test_framework import generic_test

import heapq
# def merge_sorted_arrays(arrs: List[List[int]]) -> List[int]:
#     ans = []
#     minheap = []
#     for arr_i in range(len(arrs)):
#         heapq.heappush(minheap,(arrs[arr_i][0],arr_i,0))

#     while minheap:
#         val,arr_i,idx=heapq.heappop(minheap)
#         ans.append(val)
#         next_idx = idx+1
#         if next_idx<len(arrs[arr_i]):
#             next_val = arrs[arr_i][next_idx]
#             heapq.heappush(minheap,(next_val,arr_i,next_idx))
#     return ans    


def merge_sorted_arrays(arrs: List[List[int]]) -> List[int]:
    return list(heapq.merge(*arrs))

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('sorted_arrays_merge.py',
                                       'sorted_arrays_merge.tsv',
                                       merge_sorted_arrays))
