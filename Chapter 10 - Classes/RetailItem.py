'''
Author: Gabriel dos Reis
Date: 11/2/2023
Program: RetailItem.py
Description:
Write a class named  that holds data about an item in a retail store. 
The class should store the following data in attributes: 
    ** Item description
    ** Units in inventory
    ** Price
Once you have written the class, write a program that creates three  objects and stores the following data in them:
          
Item        Description     Units in Inventory      PriceItem 
Item #1      Jacket             12                  59.95
Item #2      Designer Jeans     40                  34.95
Item #3      Shirt              20                  24.95
'''

class RetailItem():
    def __init__(self, description = "", units = 0, price = 0.0):
        self.__description = description
        self.__units = units
        self.__price = price
    
    #  Properties for each attribute to set setters and getters
    @property
    def description(self):
        return self.__description
    @description.setter
    def description(self,description):
        self.__description = description
        
    @property
    def units(self):
        return self.__units
    @units.setter
    def units(self,units):
        self.__units = units
        
    @property
    def price(self):
        return self.__price
    @price.setter
    def price(self, price):
        self.__price = price
        
    def __str__(self):
        display_string = str('{:20} {:12} {:15}'.format(self.__description, str(self.__units), str(self.__price)))
         
        return display_string