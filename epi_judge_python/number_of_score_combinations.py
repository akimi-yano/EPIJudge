from typing import List

from test_framework import generic_test

def num_combinations_for_final_score(final_score: int, individual_play_scores: List[int]) -> int:
    def helper(i, remaining):
        key = (i, remaining)
        if key in memo:
            return memo[key]
        ways = 0 
        if remaining == 0:
            ways = 1
        elif i > len(individual_play_scores)-1 or remaining < 0: # important to have this check: remaining < 0
            pass
        else:            
            ways += helper(i, remaining - individual_play_scores[i])
            ways += helper(i+1, remaining)
        memo[key] = ways
        return ways
    
    memo = {}
    return helper(0, final_score)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('number_of_score_combinations.py',
                                       'number_of_score_combinations.tsv',
                                       num_combinations_for_final_score))
