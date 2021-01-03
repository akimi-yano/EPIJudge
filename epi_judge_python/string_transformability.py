from typing import Set

from test_framework import generic_test

# This solution works
from collections import deque
def transform_string(D: Set[str], s: str, t: str) -> int:
    if (s not in D) or (t not in D):
        return -1
    queue = deque([(s, 0)])
    seen  = set([])
    while queue:
        word, step = queue.popleft()
        if word == t:
            return step
        if word in seen:
            continue
        seen.add(word)
        for j in range(len(word)):
            for i in range(26):
                letter = chr(ord('a')+i)
                new_word = word[:j] + letter + word[j+1:]
                if (new_word in D) and (new_word not in seen):
                    queue.append((new_word, step+1))
    return -1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('string_transformability.py',
                                       'string_transformability.tsv',
                                       transform_string))
