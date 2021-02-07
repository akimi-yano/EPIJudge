from typing import List

from test_framework import generic_test, test_utils

# This solution works:
# def generate_balanced_parentheses(num_pairs: int) -> List[str]:
    # ans = []
    
    # def helper(arr, opened, remaining):
    #     if remaining == 0 and opened == 0:
    #         ans.append("".join(arr))
    #         return
    #     elif remaining <= 0:
    #         return
    #     if opened < remaining:
    #         helper(arr+["("], opened+1, remaining)
    #     if opened:
    #         helper(arr+[")"], opened-1, remaining-1)
    # helper([], 0, num_pairs)
    # return ans

# This solution works:
def generate_balanced_parentheses(num_pairs: int) -> List[str]:
    ans = []
    
    def helper(arr, opened, remaining):
        if remaining == 0 and opened == 0:
            ans.append("".join(arr))
            return
        elif remaining <= 0:
            return
        
        if opened < remaining:
            arr.append("(")
            helper(arr, opened+1, remaining)
            arr.pop()
            
        if opened:
            arr.append(")")
            helper(arr, opened-1, remaining-1)
            arr.pop()
            
    helper([], 0, num_pairs)
    return ans


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('enumerate_balanced_parentheses.py',
                                       'enumerate_balanced_parentheses.tsv',
                                       generate_balanced_parentheses,
                                       test_utils.unordered_compare))
