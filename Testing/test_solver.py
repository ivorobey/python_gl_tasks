import unittest
from unittest import TestCase
from solver import *

class TestAddCase(TestCase):
    def test_01_add(self):
        res=add(1,2)
        self.assertEqual(res,3)

class TestSquareEquationSolver(TestCase):
    def test_02_reises_types(self):
        with self.assertRaises(TypeError):
            square_equation_solver("",1,1.5)

    def test_03_res_is_tuple(self):
        res=square_equation_solver(0,0,0)
        self.assertIsInstance(res,tuple)

    def test_03_noresults(self):
        res=square_equation_solver(0,0,1)
        self.assertEqual(res,(None,None))
        


if __name__=='__main__':
    unittest.main()
