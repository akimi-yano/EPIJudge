from test_framework import generic_test


def snake_string(s: str) -> str:
    even = []
    odd = []
    for i in range(len(s)):
        if i % 2 == 0:
            even.append(s[i])
        else:
            odd.append(s[i])
    first = []
    third = []
    for i in range(len(odd)):
        if i % 2 == 0:
            first.append(odd[i])
        else:
            third.append(odd[i])
    return "".join(first +  even +  third)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('snake_string.py', 'snake_string.tsv',
                                       snake_string))
