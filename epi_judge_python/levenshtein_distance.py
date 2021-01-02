from test_framework import generic_test


def levenshtein_distance(A: str, B: str) -> int:
    
    def helper(a, b):
        key = (a, b)
        if key in memo:
            return memo[key]
        
        min_op = float('inf')
        if b  > len(B)-1:
            # a might not be done so return the leftover from a
            min_op =  len(A)-a
        elif a > len(A)-1:
            # add only 
            min_op = min(min_op, 1 + helper(a, b+1))
        else:    
            if A[a] != B[b]: 
                # add 
                min_op = min(min_op, 1 + helper(a, b+1))
                
                # remove 
                min_op = min(min_op, 1 + helper(a+1, b))
                
                # swap 
                min_op = min(min_op, 1 + helper(a+1, b+1)) 
            else:
                # do nothing 
                min_op = min(min_op, helper(a+1, b+1))
        
        memo[key] = min_op
        return min_op
    
    memo = {}
    return helper(0, 0)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('levenshtein_distance.py',
                                       'levenshtein_distance.tsv',
                                       levenshtein_distance))
