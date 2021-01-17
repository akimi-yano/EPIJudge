from test_framework import generic_test


def is_well_formed(s: str) -> bool:
    stack = []
    closing = set([')',']','}'])
    open_pairs = {'(':')', '[':']', '{':'}'}
    for elem in s:
        if elem in open_pairs:
            stack.append(elem)
        elif elem in closing:
            if not stack:
                return False
            opening = stack.pop()
            if opening not in open_pairs:
                return False
            if open_pairs[opening] != elem:
                return False
    return not stack


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_valid_parenthesization.py',
                                       'is_valid_parenthesization.tsv',
                                       is_well_formed))
