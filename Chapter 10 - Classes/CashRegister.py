'''
Author: Gabriel dos Reis
Date: 11/2/2023
Program: CashRegister.py
Description:
Create a CashRegister class that can be used with the RetailItem class. 
The CashRegister class should be able to internally keep a list of RetailItem objects. 
The class should have the following methods:
    • purchase_item that accepts a RetailItem object as an argument. 
        Each time the purchase_item method is called, the RetailItem object that is passed as an argument should be added to the list. 
    • get_total that returns the total price of all the RetailItem objects stored in the CashRegister object’s internal list. 
    • show_items that displays data about the RetailItem objects stored in the CashRegister object’s internal list. 
    • clear that should clear the CashRegister object’s internal list. 
Demonstrate the CashRegister class in a program that allows the user to select several items for purchase. When the user is ready 
to check out, the program should display a list of all the items he or she has selected for purchase, as well as the total price.
'''

class CashRegister():
    
    # Class constant that represents 7.5% of tax
    TAX_RATE = 0.075

    def __init__(self):
        '''
        Constructor that initializes a list to hold the retail items
        '''
        self.items = []
    
    # Method that appends a new item to the items list
    def purchase_item(self, item):
        self.items.append(item)
    
    # Method that calculates the price of the purchase
    def get_total(self):
        total = 0
        for item in self.items:
            total += item.price * item.units
        return total
    
    # Method that calculates the tax amount to pay by calling the get_total function.
    def get_tax_amt(self):
        total_price = self.get_total()
        tax_amt = total_price * CashRegister.TAX_RATE
        return tax_amt
    
    # Method that displays the items in the items list
    def show_items(self):
        for item in self.items:
            print(item)
    
    # Method that clears the list
    def clear(self):
        self.items = []
 