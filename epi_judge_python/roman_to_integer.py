from test_framework import generic_test


def roman_to_integer(s: str) -> int:
    '''
    59
    xxxxxiiiiiiiii
    lviiii
    lix
    '''
    memo = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
    ans = 0
    prev = None
    for elem in s:
        if prev is None or prev >= memo[elem]:
            ans += memo[elem]
        else:
            ans -= prev
            ans += (memo[elem] - prev)
        prev = memo[elem]
    return ans

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('roman_to_integer.py',
                                       'roman_to_integer.tsv',
                                       roman_to_integer))
