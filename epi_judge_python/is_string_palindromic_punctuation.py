from test_framework import generic_test

# This solution works but needs optimization
# def is_palindrome(s: str) -> bool:
#     valid = set("123456789abcdefghijklmnopqrstuvwxyz")
#     s = s.lower()
#     news = ""
#     for c in s:
#         if c in valid:
#             news += c
#     left = 0
#     right = len(news)-1
#     while left < right:
#         if news[left] != news[right]:
#             return False
#         left += 1
#         right -= 1    
#     return True


# This solution works !
# Time: O(N)
# Space: O(1)
def is_palindrome(s: str) -> bool:
    left, right = 0, len(s)-1
    while left < right:
        if not s[left].isalnum():
            left += 1
        elif not s[right].isalnum(): 
            right -= 1
        elif s[left].lower() != s[right].lower():
            return False
        else:
            left += 1
            right -= 1    
    return True
    
    
if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'is_string_palindromic_punctuation.py',
            'is_string_palindromic_punctuation.tsv', is_palindrome))
