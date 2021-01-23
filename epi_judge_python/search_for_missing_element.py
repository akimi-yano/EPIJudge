import collections
from typing import List

from test_framework import generic_test
from test_framework.test_failure import PropertyName

DuplicateAndMissing = collections.namedtuple('DuplicateAndMissing',
                                             ('duplicate', 'missing'))
# this solution works
def find_duplicate_missing(A: List[int]) -> DuplicateAndMissing:
    # calculate XOR of all numbers in A
    A_xor = 0
    for num in A:
        A_xor ^= num
    
    # calculate XOR of all numbers in the range 0...N-1
    N = len(A)
    nums_xor = 0
    for num in range(N):
        nums_xor ^= num

    # "A_xor XOR nums_xor" cancels out all numbers that appear exactly one, and leaves the missing and duplicate numbers
    dup_missing_xor = A_xor ^ nums_xor
    
    # find the bit where the missing and duplicate numbers differ
    diff_bit = 1
    while dup_missing_xor & diff_bit == 0:
        diff_bit <<= 1
    
    # calculate XOR of all  numbers in A where diff_bit is set
    A_xor2 = 0
    for num in A:
        if num & diff_bit != 0:
            A_xor2 ^= num

    # calculate XOR of all numbers in the range 0...N-1 where diff_bit is set
    nums_xor2 = 0
    for num in range(N):
        if num & diff_bit != 0:
            nums_xor2 ^= num
    
    # "A_xor2 XOR nums_xor2" will leave just one number, either the missing or duplicate (we don't know which yet)
    first_number = A_xor2 ^ nums_xor2
    # second_number can be calculated using the dup_missing_xor
    second_number = dup_missing_xor ^ first_number
    
    for num in A:
        # if first_number appears, it is the duplicate number
        if num == first_number:
            return DuplicateAndMissing(first_number, second_number)
        # if second_number appears, it is the duplicate number
        elif num == second_number:
            return DuplicateAndMissing(second_number, first_number)
    assert False
    
    # mask = 1
    # while not (mask & xor):
    #     mask <<= 1
    # xor2 = 0
    # for i, num in enumerate(A):
    #     if i & mask:
    #         xor2 ^= i
    #     if num & mask:
    #         xor2 ^= num
    # for num in A:
    #     if num == xor2:
    #         return DuplicateAndMissing(xor2, xor2 ^ xor)
    # return DuplicateAndMissing(xor ^ xor2, xor2)
    
# This solution works
# from collections import Counter
# def find_duplicate_missing(A: List[int]) -> DuplicateAndMissing:
#     counts = Counter(A)
#     N = len(A)
#     dup = None
#     for key, value in counts.items():
#         if value == 2:
#             dup = key 
#             break
#     missing = None
#     for i in range(N):
#         if counts[i] == 0:
#             missing = i
#             break
#     return DuplicateAndMissing(dup, missing)


def res_printer(prop, value):
    def fmt(x):
        return 'duplicate: {}, missing: {}'.format(x[0], x[1]) if x else None

    return fmt(value) if prop in (PropertyName.EXPECTED,
                                  PropertyName.RESULT) else value


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('search_for_missing_element.py',
                                       'find_missing_and_duplicate.tsv',
                                       find_duplicate_missing,
                                       res_printer=res_printer))
