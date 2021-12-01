'''	
@Author: Aishwarya
@Date: 2021-11-29
@Title : Test cases with multiple inputs
'''
########################################################################################################

import unittest
from Calculator import Calculator

class CalculatorTest(unittest.TestCase):

    def setUp(self):
        """
        Description:Set up an instance of Calculator pior to every test execution
        Parameter: self
        Return: none
        """
        self.calc = Calculator()  
    def test_add(self):
        """
        Description:Test case function for addition
        Parameter: self
        Return: none
        """
        self.assertEqual(10, self.calc.add(3, 7), "The addition is  wrong") 

    def test_subtract(self):
        """
        Description:Test case function for subtratction
        Parameter: self
        Return: none
        """
        self.assertEqual(12, self.calc.sub(15, 3), "Subtraction is wrong")  

    def test_multiply(self):
        """
        Description:Test case function for multiplication
        Parameter: self
        Return: none
        """
        self.assertEqual(30, self.calc.mul(5, 6), "Multiplication is wrong")  

    def test_multiple_addition(self):
        """
        Description:Test case function for addition with multiple addition
        Parameter: self
        Return: none
        """
        for a in range(10):
            for b in range(10):
                with self.subTest("add " + str(a) + " and " + str(b)):
                    self.assertEqual(a+b, self.calc.add(a, b))
    
if __name__ == '__main__':
    unittest.main()