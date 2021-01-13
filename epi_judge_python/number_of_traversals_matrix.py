from test_framework import generic_test


def number_of_ways(n: int, m: int) -> int:
    def helper(row, col):
        key = (row, col)
        if key in memo:
            return memo[key]
        ways = 0
        if row == n-1 and col == m-1:
            ways = 1
        elif not (0 <= row <= n-1) or not (0 <= col <= m-1):
            pass  
        else:
            ways = helper(row+1, col) + helper(row, col+1)
        memo[key] = ways
        return ways
    memo = {}
    return helper(0, 0)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('number_of_traversals_matrix.py',
                                       'number_of_traversals_matrix.tsv',
                                       number_of_ways))
