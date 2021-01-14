from typing import Iterator

from test_framework import generic_test


def majority_search(stream: Iterator[str]) -> str:
    elem = None
    count = 0
    while True:
        try:
            val = next(stream)
            if elem is None:
                elem = val
                count += 1
            else:
                # if elem is same, increase count
                if val == elem:
                    count += 1
                # if elem is not same, and count is zero, can't decrease anymore; update elem and set count to 1
                elif count == 0:
                    elem = val
                    count = 1
                # if elem is not same, and count is > 0, keep decrementing.
                else:
                    count -= 1
        except StopIteration:
            break
    return elem


def majority_search_wrapper(stream):
    return majority_search(iter(stream))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('majority_element.py',
                                       'majority_element.tsv',
                                       majority_search_wrapper))
