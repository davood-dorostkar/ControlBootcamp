import numpy as np
from control import ctrb
from numpy.linalg import matrix_rank
from numpy.linalg import eig
from controllability import CtrbCheck
from gramian_ctrb import GetGramianCtrb
pi = np.pi
# ===============================================
m = 1
M = 5
L = 2
g = -10
d = 1
s = 1  # the switch. upward = 1, downward = -1

A = [[0, 1, 0, 0],
     [0, -d/M, -m*g/M, 0],
     [0, 0, 0, 1],
     [0, -s*d/(M*L), -s*(m+M)*g/(M*L), 0]]
B = np.array([0, 1/M, 0, s/(M*L)]).transpose()

# ===============================================
# tspan = range(0, 5, 0.1)
# y0 = np.array([0, 0, pi, 0.5]).transpose()
# ode45
# for k in t
#   draw cart pend
# ===============================================

if __name__ == '__main__':
    eigVal, eigVec = eig(A)
    print('\nEigenvalues: \n', eigVal)
    print(ctrb(A, B))
#     print(CtrbCheck(A, B))
