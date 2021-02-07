from typing import List

from test_framework import generic_test

# This solution works! - dp bottom up + memoization
from functools import lru_cache
def longest_nondecreasing_subsequence_length(A: List[int]) -> int:
    '''
	A:        [13, 10, 8, 9, 11, 10, 8, 10, 7, 6, 2, 11, 13]
    ANS = 6            x  x       x      x            x   x
    [,]
    '''
    @lru_cache(None)
    def helper(i, prev):
        if i > len(A)-1:
            return 0
        max_len = helper(i+1, prev)
        if A[i] >= prev:
            max_len = max(max_len, 1+ helper(i+1, A[i]))
        return max_len
    return helper(0, float('-inf'))
    
    
    
    # This approach does not work: - this works for contiguous sequence not for subsequence
    # stack = []
    # best_length = 0
    # for num in A:
    #     if not stack or stack[-1] <= num:
    #         stack.append(num)
    #     else:
    #         while stack and num < stack[-1]:
    #             stack.pop()
    #         stack.append(num)
    #     best_length = max(best_length, len(stack))
    # return best_length


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'longest_nondecreasing_subsequence.py',
            'longest_nondecreasing_subsequence.tsv',
            longest_nondecreasing_subsequence_length))
