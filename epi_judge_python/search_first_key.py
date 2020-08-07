from typing import List

from test_framework import generic_test


def search_first_of_k(arr: List[int], key: int) -> int:
    lo,hi = 0, len(arr)-1
    while lo<=hi:
        mid = (lo+hi)//2
        if arr[mid] == key and (mid==0 or arr[mid-1]!=key):
            return mid
        elif arr[mid] == key and (mid!=0 and arr[mid-1]==key):
            hi  = mid-1
        else:
            lo = mid+1
    return  -1

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('search_first_key.py',
                                       'search_first_key.tsv',
                                       search_first_of_k))
