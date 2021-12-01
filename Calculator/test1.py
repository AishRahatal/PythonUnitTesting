'''	
@Author: Aishwarya
@Date: 2021-11-29
@Title : Test cases
'''
########################################################################################################

import unittest
from Calculator import Calculator#Test cases to test Calulator methods
#You always create  a child class derived from unittest.TestCase
class TestCalculator(unittest.TestCase):
  
    def test_add(self):
        """
        Description:Test case function for addition
        Parameter: self
        Return: none
        """
        
        self.calc = Calculator()
        result = self.calc.add(4, 7)
        expected = 11
        self.assertEqual(result, expected)

    def test_sub(self):
        """
        Description:Test case function for subtratction
        Parameter: self
        Return: none
        """
        self.calc = Calculator()
        result = self.calc.sub(10, 5)
        expected = 5
        self.assertEqual(result, expected)

    #@unittest.skip('Some reason')
    def test_mul(self):
        """
        Description:Test case function for multiplication
        Parameter: self
        Return: none
        """
        self.calc = Calculator()
        result = self.calc.mul(3, 7)
        expected = 21
        self.assertEqual(result, expected)

    @unittest.skip('gives error due to number divide by 0')
    def test_division(self):
        """
        Description:Test case function for division
        Parameter: self
        Return: none
        """
        self.calc = Calculator()
        result = self.calc.div(10, 0)
        expected = 0
        self.assertEqual(result, expected)

    def test_div(self):
        """
        Description:Test case function for division
        Parameter: self
        Return: none
        """
        self.calc = Calculator()
        self.assertEqual(self.calc.div(10, 5), 2)
        self.assertEqual(self.calc.div(12, 2), 6)

    def test_div_error(self):
        """
        Description:Make sure ZeroDivisionError is raised when necessar
        Parameter: self
        Return: none
        """
        self.calc = Calculator()
        self.assertRaises(ZeroDivisionError, self.calc.div, 10, 0)    

    
        
if __name__ == "__main__":
  unittest.main()