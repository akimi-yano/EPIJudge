from test_framework import generic_test


def parity(x: int) -> int:
    # TODO - you fill in here.

    # Approach 1: count the number of ans
    # ans = 0
    # while x:
    #     ans += x&1
    #     x >>= 1
    # return ans%2

    # Approach 2: use xor as we only care about if the ans is even of odd
    # ans = 0
    # while x:
    #     ans ^= x&1
    #     x >>= 1
    # return ans

    # Approach 3: reduce the time complexity by removing 1s bit
    ans = 0
    while x:
        ans ^= 1 # since we know it is 1
        x &= x-1 # drop the lowest set bit of x
    return ans

if __name__ == '__main__':
    exit(generic_test.generic_test_main('parity.py', 'parity.tsv', parity))
