# from numpy.linalg import svd
from scipy.linalg import svd
from control import ctrb

A1 = [[1, 0], [0, 2]]
B1 = [[0], [1]]

A2 = [[1, 1], [0, 2]]
B2 = [[0], [1]]


def GetGramianCtrb(a, b):
    c = ctrb(a, b)
    u, s, v = svd(c)
    print('\nGramian eig vectors: \n\n', u)
    print('\nGramian eig values: \n\n', s)
    print('======================\n')


if __name__ == '__main__':
    GetGramianCtrb(A1, B1)
    GetGramianCtrb(A2, B2)
