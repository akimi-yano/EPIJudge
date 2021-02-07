from typing import List

from test_framework import generic_test

import heapq
def generate_first_k_a_b_sqrt2(k: int) -> List[float]:
    seen = set([])
    a = b = 0
    minheap = []
    heapq.heappush(minheap, (a+b*2**(1/2), a, b))
    ans = []
    while minheap:
        val, a, b = heapq.heappop(minheap)
        if (a, b) in seen:
            continue
        seen.add((a, b))
        
        if k:
            ans.append(val)
            k -= 1
        else:
            return ans
        
        if (a+1, b) not in seen:
            heapq.heappush(minheap, ((a+1)+b*2**(1/2), a+1, b))
        if (a, b+1) not in seen:
            heapq.heappush(minheap, (a+(b+1)*2**(1/2), a, b+1))



if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('a_b_sqrt2.py', 'a_b_sqrt2.tsv',
                                       generate_first_k_a_b_sqrt2))
