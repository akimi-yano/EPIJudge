from test_framework import generic_test


def square_root(k: int) -> int:
    left = 0
    right = k
    while left < right:
        mid = (left + right +1) //2
        if mid ** 2 <= k:
            left = mid
        else:
            right = mid - 1
    return left


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('int_square_root.py',
                                       'int_square_root.tsv', square_root))
