'''
Author: Gabriel dos Reis
Date: 11/1/2023
Program: Personal_info.py
Description:
Design a class that holds the following personal data:
  * Name
  * Address
  * Age
  * Phone number

Write appropriate accessor and mutator methods. 
Also, write a program that creates three instances of the class. 
One instance should hold your information, and the other two should hold your friends’ or family members’ information.
'''

class PersonalInfo():
  def __init__(self, name, address, phone_num, age = 0):
    self.__name = name
    self.__address = address
    self.__age = age
    self.__phone_num = phone_num
    
  # Setters
  def set_name(self, name):
    self.__name = name
  
  def set_address(self, address):
    self.__address = address
    
  def set_age(self, age):
    self.__age = age
    
  def set_phone_num(self, phone_num):
    self.__phone_num = phone_num
    
  # Getters
  def get_name(self):
    return self.__name
  
  def get_address(self):
    return self.__address
  
  def get_age(self):
    return self.__age
  
  def get_phone_num(self):
    return self.__phone_num
  
  def __str__(self):
    info = f"Name: {self.__name}\tAge: {str(self.__age)}\nAddress: {self.__address}\tPhone number: {self.__phone_num}\n"
    
    return info
    
if __name__ == "__main__":
    
    personal_info_dct = {}
    qtty = int(input("How many people would you like to add information?: "))
    
    # Prompt user for the name, address, age, and phone number of the person and add to the list
    for x in range(qtty):
      name = input("\nEnter person's name: \n")
      address = input("Enter person's address: \n")
      age = int(input("Enter person's age: \n"))
      phone_num = input("Enter person's phone number: \n")
        
      # Create an instance of the PersonalInfo object
      person = PersonalInfo(name, address, age, phone_num)
        
      personal_info_dct[name] = person    
    # Loop to display the information
    for name, person in personal_info_dct.items():
      print(f"Information from {name}")
      print(person)
    print()