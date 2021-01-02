from typing import List

from test_framework import generic_test


def n_queens(n: int) -> List[List[int]]:
    # n is # of queens and matrix of size n * n
    def helper(arr):
        nonlocal n
        if len(arr) == n:
            ans.append(arr)
            return 
        banned = set(arr)
        nextidx = len(arr)
        for i in range(len(arr)):
            banned.add(arr[i] + (nextidx - i))
            banned.add(arr[i] - (nextidx - i))
        for num in range(n): 
            if not arr or (arr and (abs(num - arr[-1]) >= 2) and num not in banned):
                helper(arr + [num])
            
    ans = []
    helper([])
    return ans


def comp(a, b):
    return sorted(a) == sorted(b)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('n_queens.py', 'n_queens.tsv', n_queens,
                                       comp))
