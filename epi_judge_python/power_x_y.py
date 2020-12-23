from test_framework import generic_test

# This approach works but maybe this is not what is expected
# def power(x: float, y: int) -> float:
#     return x ** y

def power(x: float, y: int) -> float:
    result =  1.0
    power = y
    if power < 0:
        power = -power
        x = 1.0/x
    while power:
        # if power is odd number:
        # if power & 1:
        if power % 2 != 0:
            result *= x
        # x -> x**2 and power -> divide by 2 (integer division) or bit right shift by 1
        # x, power = x * x, power >> 1
        x, power = x * x, power // 2
    return result
if __name__ == '__main__':
    exit(generic_test.generic_test_main('power_x_y.py', 'power_x_y.tsv',
                                        power))
