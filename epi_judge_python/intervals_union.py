import collections
import functools
from typing import List

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook

Endpoint = collections.namedtuple('Endpoint', ('is_closed', 'val'))

Interval = collections.namedtuple('Interval', ('left', 'right'))


def union_of_intervals(intervals: List[Interval]) -> List[Interval]:
    intervals.sort(key=lambda interval: (interval.left.val, 0 if interval.left.is_closed else 1))
    ans = []
    
    cur_start, cur_end = intervals[0]
    for next_start, next_end in intervals[1:]:
        # if the next interval is not connected
        if cur_end.val < next_start.val or \
            (cur_end.val == next_start.val and not cur_end.is_closed and not next_start.is_closed):
            interval = Interval(cur_start, cur_end)
            ans.append(interval)
            cur_start = next_start
            cur_end = next_end
        # if the next interval is connected
        else:
            cur_end = max(cur_end, next_end, key=lambda endpoint:(endpoint.val, 1 if endpoint.is_closed else 0 ))
    ans.append(Interval(cur_start, cur_end))
    return ans


@enable_executor_hook
def union_of_intervals_wrapper(executor, intervals):
    intervals = [
        Interval(Endpoint(x[1], x[0]), Endpoint(x[3], x[2])) for x in intervals
    ]

    result = executor.run(functools.partial(union_of_intervals, intervals))

    return [(i.left.val, i.left.is_closed, i.right.val, i.right.is_closed)
            for i in result]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('intervals_union.py',
                                       'intervals_union.tsv',
                                       union_of_intervals_wrapper))
