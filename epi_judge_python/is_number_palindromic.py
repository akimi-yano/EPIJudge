from test_framework import generic_test

import math

def is_palindrome_number(x: int) -> bool:

    # if x is a negative number, it's False due to the '-' sign
    if x <=0:
        return x == 0
    
    # formula to get the number of digits (basically same as int diviging it by 10 until it becomes smaller than 0)
    num_digits = math.floor(math.log10(x)) + 1 
    # made a mask to filter to check and remove digits
    msd_mask = 10**(num_digits - 1)

    for _ in range(num_digits // 2):
        if x // msd_mask != x % 10: 
            return False
    
        x %= msd_mask # Remove the most significant digit of x 
        x //= 10 # Remove the least significant digix of x. 
        # reducing the 2 digits after checking if they are palindrome
        msd_mask //= 100
    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_number_palindromic.py',
                                       'is_number_palindromic.tsv',
                                       is_palindrome_number))
