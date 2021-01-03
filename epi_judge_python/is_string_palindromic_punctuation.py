from test_framework import generic_test


def is_palindrome(s: str) -> bool:
    valid = set("123456789abcdefghijklmnopqrstuvwxyz")
    s = s.lower()
    news = ""
    for c in s:
        if c in valid:
            news += c
    left = 0
    right = len(news)-1
    while left < right:
        if news[left] != news[right]:
            return False
        left += 1
        right -= 1    
    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'is_string_palindromic_punctuation.py',
            'is_string_palindromic_punctuation.tsv', is_palindrome))
