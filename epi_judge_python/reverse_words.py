import functools

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook


# Assume s is a list of strings, each of which is of length 1, e.g.,
# ['r', 'a', 'm', ' ', 'i', 's', ' ', 'c', 'o', 's', 't', 'l', 'y'].


# This solution works !
# Time: O(N)
# Space:O(1)
def reverse_words(s):
    s.reverse()
    start = idx = 0
    while idx < len(s):
        if s[idx] != ' ':
            idx += 1
        else:
            end = idx -1
            while start < end:
                s[start], s[end] = s[end], s[start]
                start += 1
                end -= 1
            start = idx = idx + 1
    end = idx -1
    while start < end:
        s[start], s[end] = s[end], s[start]
        start += 1
        end -= 1
    return s
        
        
        
        
@enable_executor_hook
def reverse_words_wrapper(executor, s):
    s_copy = list(s)

    executor.run(functools.partial(reverse_words, s_copy))

    return ''.join(s_copy)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('reverse_words.py', 'reverse_words.tsv',
                                       reverse_words_wrapper))
