import unittest
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from inverted_pendulum import CartPendulum


class CartTester(unittest.TestCase):
    def test_null(self):
        pass


if __name__ == "__main__":
    unittest.main()
