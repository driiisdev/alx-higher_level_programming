#!/usr/bin/python3

"""
This module supplies the function matrix_mul.
"""


def matrix_mul(m_a, m_b):
    """
    Performs matrix multiplication on two matrices (list of lists) 
    """
    if isinstance(m_a, list):
        if len(m_a) == 0:
            raise ValueError("m_a can't be empty")
        else:
            for a in m_a:
                if not isinstance(a, list):
                    raise TypeError("m_a must be a list of lists")
                elif len(a) == 0:
                    raise ValueError("m_a can't be empty")
                else:
                    for i in a:
                        if not isinstance(i, (int, float)):
                            raise TypeError("m_a should contain only \
integers or floats")
    else:
        raise TypeError("m_a must be a list")
    if isinstance(m_b, list):
        if len(m_b) == 0:
            raise ValueError("m_b can't be empty")
        else:
            for b in m_b:
                if not isinstance(b, list):
                    raise TypeError("m_b must be a list of lists")
                elif len(b) == 0:
                    raise ValueError("m_b can't be empty")
                else:
                    for j in b:
                        if not isinstance(j, (int, float)):
                            raise TypeError("m_b should contain only \
integers or floats")
    else:
        raise TypeError("m_b must be a list")

    x = len(m_a[0])
    y = len(m_b[0])
    for a in m_a:
        if len(a) != x:
            raise TypeError("each row of m_a must be of the same size")
    for b in m_b:
        if len(b) != y:
            raise TypeError("each row of m_b must be of the same size")
    if x != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    mul = []
    for a in m_a:
        inmul = []
        for p in range(len(m_b[0])):
            m = 0
            q = 0
            for b in m_b:
                m += b[p] * a[q]
                q += 1
            p += 1
            inmul.append(m)
        mul.append(inmul)
    return mul
