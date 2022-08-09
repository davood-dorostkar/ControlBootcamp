import unittest
import os
import sys
import numpy as np
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from inverted_pendulum import CartPendulum
PI = np.pi


class CartTester(unittest.TestCase):
    def setUp(self) -> None:
        self.initCondition = [0, 0, PI, 0.5]
        self.u = 0

    def test_null(self):
        pass

    def test_can_init_log(self):
        cp = CartPendulum(self.initCondition, self.u)
        self.assertEqual(cp.y_log, [[0, 0, 0, 0]])


if __name__ == "__main__":
    unittest.main()
