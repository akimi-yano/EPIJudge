from test_framework import generic_test


def reverse(num: int) -> int:
    ans =0
    is_negative = False
    if num<0:
        is_negative = True
        num=num*(-1)
    while num:
        ans=ans*10
        ans+=(num%10)
        num=num//10
    return ans*(-1) if is_negative else ans 


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('reverse_digits.py',
                                'reverse_digits.tsv', reverse))
