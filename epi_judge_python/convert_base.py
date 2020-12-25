from test_framework import generic_test


def convert_base(num_as_string: str, b1: int, b2: int) -> str:
    base_str_to_int = {  '0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7,
                    '8': 8, '9': 9, 'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15    }
    int_to_base_str =  {  0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7',
                    8: '8', 9: '9', 10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'    }
    
    # convert form b1 to base 10
    digit = 0
    b10_total = 0
    negative = False
    if num_as_string[0] == '-':
        num_as_string = num_as_string[1:]
        negative = True
    for char in reversed(num_as_string):
        b10_total += base_str_to_int[char] * b1 ** digit 
        digit += 1
    
    # convert from base 10 to b2 
    b2_total = ""
    while b10_total:
        quotient, remainder = divmod(b10_total, b2)
        b2_total = int_to_base_str[remainder] + b2_total
        b10_total = quotient
    if len(b2_total) == 0:
        b2_total = '0'
    if negative:
        b2_total = '-' + b2_total
    return b2_total


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('convert_base.py', 'convert_base.tsv',
                                       convert_base))
