from test_framework import generic_test


def evaluate(expression: str) -> int:
    nums = expression.split(',')
    arr = []
    for x in nums:
        if x.isdigit():
            arr.append(int(x))
        elif x in ('+','-','*','/'):
            num2 = arr.pop()
            num1 = arr.pop()
            if x == '+':
                arr.append(num1 + num2)
            elif x == '-':
                arr.append(num1 - num2)
            elif  x == '*':
                arr.append(num1 * num2)
            elif x == '/':
                arr.append(num1 // num2)

    return arr[0] if arr else 0

# 11+8*10+7*12+12*7+9*14+17
# 11 + 80 + 84 + 84 + 126 + 17
# 91 + 168 + 143 = 259 + 143 = 402

# 402


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('evaluate_rpn.py', 'evaluate_rpn.tsv',
                                       evaluate))
