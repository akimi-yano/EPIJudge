import functools
from typing import List

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


# This approach does not work - TLE:
# def gray_code(num_bits: int) -> List[int]:

#     def helper(arr):
#         nonlocal ans, num_bits, seen
#         if len(arr) == 2**num_bits:
#             ans = list(arr)
#             return
#         num = arr[-1]
#         for i in range(num_bits):
#             next_num = num ^ (1 << i)
#             if next_num not in seen:
#                 arr.append(next_num)
#                 seen.add(next_num)
#                 helper(arr)
#                 arr.pop()
#                 seen.remove(next_num)
#     ans = []
#     seen = set([0])
#     helper([0])
#     return ans

def gray_code(num_bits: int) -> List[int]:
    if num_bits == 0:
        return [0]

    def helper(n):
        if n == 1:
            return [0, 1]

        # [0,1,3,2]
        first_half = helper(n-1)
        #[000, 001, 011, 010]

        second_half = []
        # [2,3,1,0]
        # [010, 011, 001, 000]
        # 2 | (1<<2) = 10 | 100 = 110
        for num in reversed(first_half):
            second_half.append(num | (1 << (n-1)))
        return first_half + second_half

    return helper(num_bits)


def differ_by_1_bit(a, b):
    x = a ^ b
    if x == 0:
        return False
    while x & 1 == 0:
        x >>= 1
    return x == 1

@enable_executor_hook
def gray_code_wrapper(executor, num_bits):
    result = executor.run(functools.partial(gray_code, num_bits))

    expected_size = (1 << num_bits)
    if len(result) != expected_size:
        raise TestFailure('Length mismatch: expected ' + str(expected_size) +
                          ', got ' + str(len(result)))
    for i in range(1, len(result)):
        if not differ_by_1_bit(result[i - 1], result[i]):
            if result[i - 1] == result[i]:
                raise TestFailure('Two adjacent entries are equal')
            else:
                raise TestFailure(
                    'Two adjacent entries differ by more than 1 bit')

    uniq = set(result)
    if len(uniq) != len(result):
        raise TestFailure('Not all entries are distinct: found ' +
                          str(len(result) - len(uniq)) + ' duplicates')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('gray_code.py', 'gray_code.tsv',
                                       gray_code_wrapper))
