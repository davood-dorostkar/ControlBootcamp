import numpy as np
from control import ctrb
from numpy.linalg import matrix_rank
from numpy.linalg import eig
from controllability import CtrbCheck
from gramian_ctrb import GetGramianCtrb
import matplotlib.pyplot as plt
PI = np.pi
# ===============================================


def SystemAnalyse(A, B):
    eigVal, eigVec = eig(A)
    print('\nEigenvalues: \n', eigVal)
    print('\nControllability: \n', ctrb(A, B))
    CtrbCheck(A, B)
    GetGramianCtrb(A, B)


class CartPendulum:
    def __init__(self, init, input):
        self.m = 1
        self.M = 5
        self.L = 2
        self.g = -10
        self.d = 1
        self.s = 1  # the switch. upward = 1, downward = -1
        self.dy = [[0]]*4
        self.y = init
        self.y_log = [0]*4
        self.u = input
        self.StateSpace(self.m, self.M, self.L, self.g, self.d, self.s)
# ===============================================

    def StateSpace(self, m, M, L, g, d, s):
        self.A = [[0, 1, 0, 0],
                  [0, -d/M, -m*g/M, 0],
                  [0, 0, 0, 1],
                  [0, -s*d/(M*L), -s*(m+M)*g/(M*L), 0]]
        self.B = [[0], [1/M], [0], [s/(M*L)]]

# ===============================================

    def DynamicsIncrement(self, y, m, M, L, g, d, u):
        dy = [0]*4
        Sy = np.sin(y[2])
        Cy = np.cos(y[2])
        D = (m*L**2)*(M+m*(1-Cy**2))
        dy[0] = y[1]
        dy[1] = (1/D)*(-m**2*L**2*g*Cy*Sy + m*L**2*(m*L*y[3]**2*Sy-d*y[1]))+m*L**2*(1/D)*u
        dy[2] = y[3]
        dy[3] = (1/D)*((m+M)*m*g*L*Sy - m*L*Cy*(m*L*y[3]**2*Sy - d*y[1]))-m*L*Cy*(1/D)*u
        return dy
# ===============================================

    def Integrate(self, y, dy, t, t_prev):
        dt = t - t_prev
        y_next = y + np.array(dy)*dt
        return y_next
# ===============================================

    def SaveState(self):
        self.y_log.append(self.y)
# ===============================================

    def Solve(self, thisTime, prevTime):
        self.dy = self.DynamicsIncrement(self.y, self.m, self.M, self.L, self.g, self.d, self.u)
        self.y = self.Integrate(self.y, self.dy, thisTime, prevTime)

    def Visualize(self):
        tspan = np.linspace(0, 30, len(self.y_log))
        # for iter in self.y_log:
        # print(len(iter))
        # print(type(iter))
        # print(iter[0])
        # log = np.array(self.y_log)
        print(self.y_log.shape)
        print(tspan.shape)
        # print(len(tspan))
        # plt.figure()
        # plt.plot(tspan, self.y_log)
        # plt.show()


if __name__ == '__main__':
    stop = 30
    increment = 0.01
    initCondition = [0, 0, PI, 0.5]
    u = 0
    cart = CartPendulum(initCondition, u)
    cart.SaveState()
    lastTime = 0
    while lastTime < stop:
        thisTime = lastTime + increment
        cart.Solve(thisTime, lastTime)
        cart.SaveState()
        lastTime = thisTime
    # cart.Visualize()
