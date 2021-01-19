import unittest
from unittest import TestCase
from solver import *

class TestAddCase(TestCase):
    def test_01_add(self):
        res=add(1,2)
        self.assertEqual(res,3)

class TestSquareEquationSolver(TestCase):
    def test_02_reises_types(self):
        try:
            square_equation_solver("1",1,1.5)
        except TypeError as e:
            print("Ok, eror ",e)
        else:
            self.fail("Did not raise")


if __name__=='__main__':
    unittest.main()
