from test_framework import generic_test

import collections 

# Solution 1:
# def is_letter_constructible_from_magazine(letter: str,
#                                         magazine: str) -> bool:
#     l_d = {}
#     m_d = {}
#     for l in letter:
#         if l not  in l_d:
#             l_d[l]=1
#         else:
#             l_d[l]+=1
#     for m in magazine:
#         if m not in m_d:
#             m_d[m]=1
#         else:
#             m_d[m]+=1
#     for k,v in l_d.items():
#         if k in m_d and v<=m_d[k]:
#             pass
#         else:
#             return False
#     return True

# Solution 2:
# def is_letter_constructible_from_magazine(letter_text: str,
#                                         magazine_text: str) -> bool:
#     char_frequency_for_letter =  collections.Counter(letter_text)
    
#     for c in magazine_text:
#         if c in char_frequency_for_letter:
#             char_frequency_for_letter[c]-=1
#             if char_frequency_for_letter[c]==0:
#                 del char_frequency_for_letter[c]
#                 if not char_frequency_for_letter:
#                     return True
#     return not char_frequency_for_letter

# Solution 3:
def is_letter_constructible_from_magazine(letter_text,magazine_text):
    return (not collections.Counter(letter_text)-collections.Counter(magazine_text))



if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'is_anonymous_letter_constructible.py',
            'is_anonymous_letter_constructible.tsv',
            is_letter_constructible_from_magazine))
