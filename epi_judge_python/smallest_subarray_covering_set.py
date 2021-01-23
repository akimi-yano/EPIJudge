import collections
import functools
from typing import List, Set

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

Subarray = collections.namedtuple('Subarray', ('start', 'end'))

# this solution works !
def find_smallest_subarray_covering_set(paragraph: List[str], keywords: Set[str]) -> Subarray:
    # [strawberry, apple, pine, pen]  apple, pen
    # memo = {} <- counter
    # s                         e 
    
    memo = {}
    start = 0
    s_ans,  e_ans = 0, len(paragraph) - 1
    for end in range(len(paragraph)):
        if paragraph[end] in keywords:
            if paragraph[end] not in memo:
                memo[paragraph[end]] = 1
            else:
                memo[paragraph[end]] += 1
            while len(memo) == len(keywords):
                if e_ans-s_ans > end-start:
                    s_ans, e_ans = start, end
                if paragraph[start] in memo:
                    memo[paragraph[start]] -= 1
                    if memo[paragraph[start]] < 1:
                        del memo[paragraph[start]]
                start += 1
    return Subarray(s_ans, e_ans)


@enable_executor_hook
def find_smallest_subarray_covering_set_wrapper(executor, paragraph, keywords):
    copy = keywords

    (start, end) = executor.run(
        functools.partial(find_smallest_subarray_covering_set, paragraph,
                          keywords))

    if (start < 0 or start >= len(paragraph) or end < 0
            or end >= len(paragraph) or start > end):
        raise TestFailure('Index out of range')

    for i in range(start, end + 1):
        copy.discard(paragraph[i])

    if copy:
        raise TestFailure('Not all keywords are in the range')

    return end - start + 1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'smallest_subarray_covering_set.py',
            'smallest_subarray_covering_set.tsv',
            find_smallest_subarray_covering_set_wrapper))
