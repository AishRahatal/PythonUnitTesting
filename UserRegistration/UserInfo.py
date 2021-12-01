'''	
@Author: Aishwarya
@Date: 2021-11-29
@Title : User Registration
'''
########################################################################################################
import re
    
def validateName(name):
    """
    Description: If name matches with regex pattern then mehod returns true
    Parameter: self,name
    Return: name
    """
    #regex for fname is first letter capital and minimum three letter
    pattern="^[A-Z]{1}[a-z]{2,}$"
    result=re.match(pattern,name)
    if result:
        return name
    else:
        raise TypeError("name must be in string format")

def validateEmail(mail):
    """
    Description: If email matches with regex pattern then mehod returns true
    Parameter: mail
    Return: mail
    """
     #regex for validating email in format abc@gmail.com
    pattern="^[a-zA-Z0-9]+([.#_$+-][a-zA-Z0-9]+)*[@][a-zA-Z0-9]+[.][a-zA-Z]{2,3}([.][a-zA-Z]{2})?$"
    result=re.match(pattern,mail)
    if result:
        return mail
    else:
        raise ValueError("email must be in given format")

def validatePhone(phone):
    """
    Description: If phone matches with regex pattern then mehod returns true
    Parameter: phone
    Return: phone
    """
   #regex for phone numbers for all countries with country code and pattern
    pattern="((?:\+|00)[17](?: |\-)?|(?:\+|00)[1-9]\d{0,2}(?: |\-)?|(?:\+|00)1\-\d{3}(?: |\-)?)?(0\d|\([0-9]{3}\)|[1-9]{0,3})(?:((?: |\-)[0-9]{2}){4}|((?:[0-9]{2}){4})|((?: |\-)[0-9]{3}(?: |\-)[0-9]{4})|([0-9]{7}))"
    result=re.match(pattern,phone)
    if result:
        return phone
    else:
         raise ValueError("Phone number must be in given format")

def validatePassword(password):
    """
    Description: If phone matches with regex pattern then mehod returns true
    Parameter: self,password
    Return: True
    """
    #regex for password minimum 8 chacter Should have at least 1 capital letter,1 special character,1 number'
    pattern="^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[^\w\s]).{8,}$"
    result=re.match(pattern,password)
    if result:
        return password
    else:
        raise ValueError("password must be in given format includes A,a,0-9,and special characters ")
    