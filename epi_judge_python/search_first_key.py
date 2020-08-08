from typing import List

from test_framework import generic_test


def search_first_of_k(arr: List[int], key: int) -> int:
    if len(arr) < 1:
        return -1

    lo,hi = 0, len(arr)-1
    while lo<hi:
        mid = (lo+hi)//2
        if arr[mid] >= key:
            hi = mid
        else:
            lo = mid+1
    return -1 if arr[lo] != key else lo

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('search_first_key.py',
                                       'search_first_key.tsv',
                                       search_first_of_k))
