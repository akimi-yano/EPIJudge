from typing import List

from test_framework import generic_test



# Given n, return all primes up to and including n.
def generate_primes(n: int) -> List[int]:
    prime_table = [1 for _ in range(n+1)]
    if n == 0 or n == 1:
        return []
    prime_table[0] = 0
    prime_table[1] = 0
    prime_answer = []
    for i in range(2, n+1):
        if prime_table[i]:
            prime_answer.append(i)
            j = i + i
            while j < (n+1):
                if prime_table[j]:
                    prime_table[j] = 0
                j += i
    return prime_answer

# This approach works, but I am expected to do better than this
# Given n, return all primes up to and including n.
# def generate_primes(n: int) -> List[int]:
#     primes = []
#     for num in range(2, n+1):
#         for prime in primes:
#             if num % prime == 0:
#                 break
#         else:
#             primes.append(num)
#     return primes


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('prime_sieve.py', 'prime_sieve.tsv',
                                       generate_primes))
