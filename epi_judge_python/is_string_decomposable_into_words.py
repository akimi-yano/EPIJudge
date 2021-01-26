import functools
from typing import List, Set

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


# This solution works !
from functools import lru_cache
def decompose_into_dictionary_words(domain: str, dictionary: Set[str]) -> List[str]:
    
    @lru_cache(None)
    def helper(i):
        if i > len(domain) - 1:
            return ['']

        for word in dictionary:
            if word == domain[i:i+len(word)]:
                maybe_ans = helper(i+len(word))
                if len(maybe_ans) > 0:
                    maybe_ans.append(word)
                    return maybe_ans
        return []
    
    reversed_ans = helper(0)
    reversed_ans.reverse()
    if reversed_ans:
        reversed_ans.pop()
    return reversed_ans
    

# This approach does not work - TLE
# from functools import lru_cache
# def decompose_into_dictionary_words(domain: str, dictionary: Set[str]) -> List[str]:
#     '''
#     bed bat hand beyond.com
#     bed, bath, beyond, bat, hand
    
#     amanaplanacanal
#     a man a plan a canal
#     [a, man, a, plan, a canal]
#     '''
#     @lru_cache(None)
#     def helper(i, arr):
#         # print(arr, i)
#         if i > len(domain)-1:
#             return tuple(arr)
#         arr = list(arr)
#         for word in dictionary:
#             if domain[i:i+len(word)] == word:
#                 ans = helper(i+len(word), tuple(arr + [word]))
#                 if ans:
#                     return ans 
#         return ()
#     return list(helper(0 , ()))


@enable_executor_hook
def decompose_into_dictionary_words_wrapper(executor, domain, dictionary,
                                            decomposable):
    result = executor.run(
        functools.partial(decompose_into_dictionary_words, domain, dictionary))

    if not decomposable:
        if result:
            raise TestFailure('domain is not decomposable')
        return

    if any(s not in dictionary for s in result):
        raise TestFailure('Result uses words not in dictionary')

    if ''.join(result) != domain:
        raise TestFailure('Result is not composed into domain')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'is_string_decomposable_into_words.py',
            'is_string_decomposable_into_words.tsv',
            decompose_into_dictionary_words_wrapper))
