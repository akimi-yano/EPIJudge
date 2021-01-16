from test_framework import generic_test

# this solution works 
def look_and_say(n: int) -> str:
    prev = "1"
    cur = ""
    for _ in range(1, n):
        lastc = None
        count = 0
        for j in range(len(prev)):
            if  lastc != prev[j]:
                if lastc is not None:
                    cur += str(count)+lastc
                    count = 0
            count += 1 
            lastc = prev[j]
        if count:
            cur += str(count)+lastc
        prev = cur
        cur = ""
    return prev


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('look_and_say.py', 'look_and_say.tsv',
                                       look_and_say))
