from typing import Iterator
from itertools import tee

from test_framework import generic_test
from test_framework.test_failure import TestFailure

def find_missing_element(stream: Iterator[int]) -> int:
    '''
    10101 >> 2: 101
    101 << 2 : 10100
    '''
    ans = 0 
    # itertools.tee copies an iterator so that it can be re-used
    # if you use an iterator to the end, you usually can't go back, so you need to make a "copy" using tee
    backup, stream = tee(stream)

    for bit_idx in range(31, -1, -1):
        num_zeros = num_ones = 0
        
        backup, stream = tee(backup)
        for ip in stream:
            # we only want to count ips that match the current ans (e.g. mask)
            if ((ip >> bit_idx) << bit_idx) != ans:
                continue
            if ip & (1 << bit_idx) > 0:
                num_ones += 1
            else:
                num_zeros += 1
        if num_ones < num_zeros:
            ans |= 1 << bit_idx
    return ans



def find_missing_element_wrapper(stream):
    try:
        res = find_missing_element(iter(stream))
        if res in stream:
            raise TestFailure('{} appears in stream'.format(res))
    except ValueError:
        raise TestFailure('Unexpected no missing element exception')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('absent_value_array.py',
                                       'absent_value_array.tsv',
                                       find_missing_element_wrapper))
