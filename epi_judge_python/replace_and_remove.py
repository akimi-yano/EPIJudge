import functools
from typing import List

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook


# This solution works - creating a new array
# def replace_and_remove(size: int, s: List[str]) -> int:
#     ans = []
#     for i in range(size):
#         c = s[i]
#         if c  == 'a':
#             ans.append('d')
#             ans.append('d')
#         elif c == 'b':
#             pass
#         else:
#             ans.append(c)
            
#     for i in range(len(ans)):
#         s[i] = ans[i]
#     return len(ans)

# This solution works - in place
def replace_and_remove(size: int, s: List[str]) -> int:
    # use write_idx and read_idx
    # size is the number of elements you read
    
    # remove b
    write_idx = 0
    final_size = 0
    for read_idx in range(size):
        if s[read_idx] == 'b':
            continue
        s[write_idx] = s[read_idx]
        write_idx += 1
        final_size += 1
        if s[read_idx] == 'a':
            final_size += 1
    while len(s) < final_size:
        s.append(None)
    # print(size, s)
    # print(final_size, write_idx)
    
    new_write_idx = final_size-1
    # iterate from the back and replace a with 2 ds
    for read_idx in range(write_idx-1, -1, -1):
        if s[read_idx] == 'a':
            s[new_write_idx] = 'd'
            new_write_idx -= 1
            s[new_write_idx] = 'd'
            new_write_idx -= 1
        else:
            s[new_write_idx] = s[read_idx]
            new_write_idx -= 1
    return final_size 

@enable_executor_hook
def replace_and_remove_wrapper(executor, size, s):
    res_size = executor.run(functools.partial(replace_and_remove, size, s))
    return s[:res_size]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('replace_and_remove.py',
                                       'replace_and_remove.tsv',
                                       replace_and_remove_wrapper))
