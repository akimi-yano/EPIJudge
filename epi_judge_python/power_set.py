from typing import List

from test_framework import generic_test, test_utils


def generate_power_set(input_set: List[int]) -> List[List[int]]:
    def helper(i, arr):
        if i > len(input_set)-1:
            return [arr]
        ans = []
        ans.extend(temp for temp in helper(i+1, arr + [input_set[i]]))
        ans.extend(temp for temp in helper(i+1, arr))
        return ans
    return helper(0, [])


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('power_set.py', 'power_set.tsv',
                                       generate_power_set,
                                       test_utils.unordered_compare))
