from typing import List

from test_framework import generic_test, test_utils


def permutations(A: List[int]) -> List[List[int]]:
    def helper(arr):
        if len(arr) == 1:
            return [arr]
        if not arr:
            return []
        ans = []
        for i in range(len(arr)):
            ans.extend([arr[i]] + temp for temp in helper(arr[:i] + arr[i+1:]))
        return ans
    return helper(A)

'''
1234
1 234
2 134
3 124
4 123





1243
1324
1342
...
2134
'''

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('permutations.py', 'permutations.tsv',
                                       permutations,
                                       test_utils.unordered_compare))
