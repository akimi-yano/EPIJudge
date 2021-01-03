from typing import List

from test_framework import generic_test


def plus_one(A: List[int]) -> List[int]:
    carry = 1 
    for i in range(len(A)-1, -1, -1):
        carry, val = divmod((A[i] + carry), 10)
        A[i] =  val
        
    # add 1 at the end
    if carry:
        A = [carry] + A
    return A


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('int_as_array_increment.py',
                                       'int_as_array_increment.tsv', plus_one))
