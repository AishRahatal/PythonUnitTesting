'''	
@Author: Aishwarya
@Date: 2021-11-29
@Title : User Registration
'''
########################################################################################################
import unittest
class Test(unittest.TestCase):
    def __init__(self):
        """
        Description: It is a counstructor 
        Parameter: self
        Return: none
        """
        pass  

    def validateName(self,name):
        """
        Description: If name matches with regex pattern then mehod returns true
        Parameter: self,name
        Return: True
        """
        try:
            #regex for fname is first letter capital and minimum three letter
            pattern="^[A-Z]{1}[a-z]{2,}$"
            #assertRegex() passes if string matches with regular expression
            self.assertRegex(name,pattern)
            return True        
        except Exception as e:
            print("Error...",e) 

    def validateEmail(self,mail):
        """
        Description: If email matches with regex pattern then mehod returns true
        Parameter: self,mail
        Return: True
        """
        try:
            #regex for validating email in format abc@gmail.com
            pattern="^[a-zA-Z0-9]+([.#_$+-][a-zA-Z0-9]+)*[@][a-zA-Z0-9]+[.][a-zA-Z]{2,3}([.][a-zA-Z]{2})?$"
            #assertRegex() passes if string matches with regular expression
            self.assertRegex(mail,pattern)
            return True        
        except Exception as e:
            print("Error...",e)

    def validatePhone(self,phone):
        """
        Description: If phone matches with regex pattern then mehod returns true
        Parameter: self,phone
        Return: True
        """
        try:
            #regex for phone numbers for all countries with country code and pattern
            pattern="((?:\+|00)[17](?: |\-)?|(?:\+|00)[1-9]\d{0,2}(?: |\-)?|(?:\+|00)1\-\d{3}(?: |\-)?)?(0\d|\([0-9]{3}\)|[1-9]{0,3})(?:((?: |\-)[0-9]{2}){4}|((?:[0-9]{2}){4})|((?: |\-)[0-9]{3}(?: |\-)[0-9]{4})|([0-9]{7}))"
            #assertRegex() passes if string matches with regular expression
            self.assertRegex(phone,pattern)
            return True        
        except Exception as e:
            print("Error...",e)      

    def validatePassword(self,password):
        """
        Description: If phone matches with regex pattern then mehod returns true
        Parameter: self,password
        Return: True
        """
        try:
            #regex for password minimum 8 chacter Should have at least 1 capital letter,1 special character,1 number'
            pattern="^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[^\w\s]).{8,}$"
            #assertRegex() passes if string matches with regular expression
            self.assertRegex(password,pattern)
            return True        
        except Exception as e:
            print("Error...",e)                          

if __name__ == "__main__":
    try:
        obj=Test()
        choice=None
        while choice !=0:
            #Choices
            print("-------------------------")
            print("---------Menu---------- ")
            print(  "1:'Validate First name'")
            print(  "2:'Validate Last name'")
            print(  "3:'Validate Email'")
            print(  "4:'Validate Phone'")
            print(  "5:'Validate Password'")
            print("-------------------")
            ch=int(input("Enter Choice:"))
            if ch==1:
                #calling validate function to validate name
                print()
                #Taking user input
                first_name=input("Enter first Name: ")
                print()
                if obj.validateName(first_name):
                    print("First name is Valid")
                else:
                    print("First name is Invalid")
            elif ch==2:
                #calling accepting Float data type Array and printing function:
                # Taking user input
                print()
                last_name=input("Enter last Name: ")
                if obj.validateName(last_name):
                    print("Last name is Valid")
                else:
                    print("Last name is Invalid")
                print()
            elif ch==3:
                #calling accepting Bool data type Array and printing function:
                    # Taking user input
                email =input("\nEnter Email: ")
                if obj.validateEmail(email):      
                    print("Email is  Valid")          
                else: 
                    print("Email is Invalid")
                print()
            elif ch==4:
                #calling accepting string data type Array and printing function:
                    print()
                    phone =input("\nEnter Phone Number : ")
                    if obj.validatePhone(phone):
                        print("Phone number is Valid")
                    else:
                        print("Phone number is Invalid") 
                    
                    print()
            elif ch==5:
                
                password =input("\nEnter Password : ")
                if obj.validatePassword(password):
                    print("Password is Valid")
                else:
                    print("Password is Invalid")    

            else:print("Invalid Choice")
            
    except Exception as e:
        print("Error...",e) 
