from test_framework import generic_test


def is_letter_constructible_from_magazine(letter: str,
                                          magazine: str) -> bool:
    l_d = {}
    m_d = {}
    for l in letter:
        if l not  in l_d:
            l_d[l]=1
        else:
            l_d[l]+=1
    for m in magazine:
        if m not in m_d:
            m_d[m]=1
        else:
            m_d[m]+=1
    for k,v in l_d.items():
        if k in m_d and v<=m_d[k]:
            pass
        else:
            return False
    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'is_anonymous_letter_constructible.py',
            'is_anonymous_letter_constructible.tsv',
            is_letter_constructible_from_magazine))
