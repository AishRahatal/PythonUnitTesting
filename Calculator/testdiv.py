'''	
@Author: Aishwarya
@Date: 2021-11-29
@Title : Test cases for division with setup() and teardown()
'''
########################################################################################################
#a setUp is defined, the test runner will run that method prior to each test.  
#if a tearDown is defined the test runner will invoke that method after each test.
import unittest
from Calculator import Calculator
class TestCalcDiv(unittest.TestCase):

    def setUp(self):
        """
        Description:Set up an instance of Calculator pior to every test execution
        Parameter: self
        Return: none
        """
        self.calc = Calculator()

    def test_div(self):
        """
        Description:Test case function for division
        Parameter: self
        Return: none
        """
        self.assertEqual(self.calc.div(10, 5), 2)
        self.assertEqual(self.calc.div(12, 2), 6)

    def test_div_error(self):
        """
        Description:Make sure ZeroDivisionError is raised when necessar
        Parameter: self
        Return: none
        """
        self.assertRaises(ZeroDivisionError, self.calc.div, 10, 0)
        
if __name__ == "__main__":
    unittest.main(argv=[''], defaultTest='TestCalcDiv', verbosity=2, exit=False)