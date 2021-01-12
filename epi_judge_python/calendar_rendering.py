import collections
import functools
from typing import List

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook

# Event is a tuple (start_time, end_time)
Event = collections.namedtuple('Event', ('start', 'finish'))


def find_max_simultaneous_events(A: List[Event]) -> int:
    if len(A) < 2:
        return 1
    largest = max(A, key = lambda x: x[1])[1]
    arr = [0 for _ in range(largest+2)]
    for start, end in A:
        arr[start] += 1
        arr[end+1] -=1
    
    best = 0
    cur = 0
    for num in arr:
        cur += num
        best = max(best, cur)
    
    return best


@enable_executor_hook
def find_max_simultaneous_events_wrapper(executor, events):
    events = [Event(*x) for x in events]
    return executor.run(functools.partial(find_max_simultaneous_events,
                                          events))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('calendar_rendering.py',
                                       'calendar_rendering.tsv',
                                       find_max_simultaneous_events_wrapper))
