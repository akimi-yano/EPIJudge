from test_framework import generic_test


# This solution works
# def square_root(x: float) -> float:
#     return x ** (1/2)

import math
def square_root(x: float) -> float:
    if x < 1:
        left = 0
        right = 1
        while left < right:
            mid = (left + right) / 2
            if math.isclose(x, mid ** 2, rel_tol=10**(-15)):
                return mid
            elif mid ** 2 < x:
                left = mid
            else:
                right = mid
        return left
    else:
        left = 1
        right = x
        while left < right:
            mid = (left + right) /2
            if math.isclose(mid ** 2, x, rel_tol=10**(-15)):
                return mid
            elif mid ** 2 > x:
                right = mid
            else:
                left = mid
        return left

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('real_square_root.py',
                                       'real_square_root.tsv', square_root))
