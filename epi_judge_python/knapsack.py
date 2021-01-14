import collections
import functools
from typing import List

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook

Item = collections.namedtuple('Item', ('weight', 'value'))


def optimum_subject_to_capacity(items: List[Item], capacity: int) -> int:
    
    def helper(i, cur_weight):
        key = (i, cur_weight)
        if key in memo:
            return memo[key]
        total = 0
        if cur_weight > capacity:
            total = float('-inf')
        elif i > len(items)-1:
            pass
        else:
            weight, value = items[i]
            total = max(total, value + helper(i+1, cur_weight + weight))
            total = max(total, helper(i+1, cur_weight))
        memo[key] = total
        return total
    memo = {}
    return helper(0, 0)


@enable_executor_hook
def optimum_subject_to_capacity_wrapper(executor, items, capacity):
    items = [Item(*i) for i in items]
    return executor.run(
        functools.partial(optimum_subject_to_capacity, items, capacity))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('knapsack.py', 'knapsack.tsv',
                                       optimum_subject_to_capacity_wrapper))
