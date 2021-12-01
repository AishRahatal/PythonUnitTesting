'''	
@Author: Aishwarya
@Date: 2021-11-29
@Last Modified:2021-11-30
@Title : Test cases
'''
########################################################################################################
import unittest
from unittest.case import skip
from UserInfo import validateName,validateEmail,validatePhone,validatePassword

class TestCaseUser(unittest.TestCase):
#positive test cases
    def test_firstname(self):
        """"
        Description: this function test firstname
        Parameter: self
        Return: None
        """
        firstname = validateName("John")
        self.assertEqual(firstname, "John")

    def test_lastname(self):
        """"
        Description: this function test  lastname
        Parameter: self
        Return: None
        """
        lastname = validateName("Doe")
        self.assertEqual(lastname, "Doe")

    def test_email(self):
        """"
        Description: this function  test  email
        Parameter: self
        Return: None
        """
        email = validateEmail("johndoe@yahoo.com")
        self.assertEqual(email, "johndoe@yahoo.com")

    def test_phone(self):
        """"
        Description: this function test  phone
        Parameter: self
        Return: None
        """
        phone = validatePhone("+919922445733")
        self.assertEqual(phone, "+919922445733")

    def test_password(self):
        """"
        Description: this function test  phone
        Parameter: self
        Return: None
        """
        passwd = validatePassword("Sqwe123#df")
        self.assertEqual(passwd, "Sqwe123#df")     

    #Negative test cases
    def test_namevalue1(self):
        self.assertRaises(TypeError,validateName,'john')
    def test_namevalue2(self):
        self.assertRaises(TypeError,validateName,'doe23')
    def test_emailValue(self):
        self.assertRaises(ValueError,validateEmail,'john@doe')
    #@unittest.skip('error not raise by valueerror')       
    def test_phoneValue(self):
        self.assertRaises(ValueError,validatePhone,"23345tr")
        
    def test_passValue(self):
     
        self.assertRaises(ValueError,validatePassword,'sdecfg')
        

if __name__=='__main__':
    unittest.main()