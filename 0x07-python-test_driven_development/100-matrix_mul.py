#!/usr/bin/python3
'''
a function that multiplies 2 matrices'''

def matrix_mul(m_a, m_b):
    '''multiplies 2 matrices'''
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")
    if len(m_a) == 0:
        raise ValueError("m_a can't be empty")
    if len(m_b) == 0:
        raise ValueError("m_b can't be empty")
    if not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")
    if not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")
    if not all(len(row) > 0 for row in m_a):
        raise ValueError("m_a can't be empty")
    if not all(len(row) > 0 for row in m_b):
        raise ValueError("m_b can't be empty")
    if not all(isinstance(num, (int, float)) for row in m_a for num in row):
        raise TypeError("m_a should contain only integers or floats")
    if not all(isinstance(num, (int, float)) for row in m_b for num in row):
        raise TypeError("m_b should contain only integers or floats")
    if not all(len(row) == len(m_a[0]) for row in m_a):
        raise TypeError("each row of m_a must be of the same size")
    if not all(len(row) == len(m_b[0]) for row in m_b):
        raise TypeError("each row of m_b must be of the same size")
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")
    m_a_row = len(m_a)
    m_a_col = len(m_a[0])
    m_b_col = len(m_b[0])
    result = [[0 for _ in range(m_b_col)] for _ in range(m_a_row)]
    for i in range(m_a_row):
        for j in range(m_b_col):
            for k in range(m_a_col):
                result[i][j] += m_a[i][k] * m_b[k][j]
    return result
