from enum import Flag
from control import ctrb
from numpy.linalg import matrix_rank
from pandas import DataFrame
A1 = [[1, 0], [0, 2]]
B1 = [[0], [1]]

A2 = [[1, 1], [0, 2]]
B2 = [[0], [1]]


def CtrbCheck(A, B):
    print(f'A= \n{DataFrame(A).to_string(index=False, header=False)}\n')
    print(f'B= \n{DataFrame(B).to_string(index=False, header=False)}\n')
    if len(A) == matrix_rank(ctrb(A, B)):
        print('is Controllable')
    else:
        print('is Uncontrollable')


CtrbCheck(A1, B1)
CtrbCheck(A2, B2)
