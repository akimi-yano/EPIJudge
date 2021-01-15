from test_framework import generic_test


# This solution works
def reverse_bits(x: int) -> int:
    ans = 0
    for i in range(32):
        ans |= ((((x & (1<<i)) << 63) >> i) >> i) | ((((x & ((1 << 63) >>i)) << i << i)) >> 63)
    return ans

# This solution works
# def reverse_bits(x: int) -> int:
#     return int(((bin(x)[2:]).zfill(64)[::-1]), base = 2)
    
    

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('reverse_bits.py', 'reverse_bits.tsv',
                                       reverse_bits))
