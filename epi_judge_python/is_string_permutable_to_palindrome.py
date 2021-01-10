from test_framework import generic_test

from collections import Counter
def can_form_palindrome(s: str) -> bool:
    counts = Counter(s)
    odd = 0
    for v in counts.values():
        if v % 2 != 0:
            odd += 1
            if odd > 1:
                return False
    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'is_string_permutable_to_palindrome.py',
            'is_string_permutable_to_palindrome.tsv', can_form_palindrome))
