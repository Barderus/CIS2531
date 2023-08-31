'''
Author: Gabriel dos Reis
Date: 8/31/2023
Description: A customer in a store is purchasing five items. 
Write a program that asks for the price of each item, 
then displays the subtotal of the sale, the amount of sales tax, and the total. 
Assume the sales tax is 7 percent (0.7).
'''
TAX_PRICE = 0.07

#I'm doing this twice. One with a loop and another as intended by the book chapter

userItem1 = float(input("Enter price of item 1: "))
userItem2 = float(input("Enter price of item 2: "))
userItem3 = float(input("Enter price of item 3: "))
userItem4 = float(input("Enter price of item 4: "))
userItem5 = float(input("Enter price of item 5: "))

ttlPrice = userItem1 + userItem2 + userItem3 + userItem4 + userItem5
salesTax = (ttlPrice * TAX_PRICE)
ttlPay = ttlPrice + salesTax
print(f"Subtotal of the sale: {ttlPrice:.2f} \nSales Tax: {salesTax:.2f}(7%) \nTotal to pay: {ttlPay:.2f}")

'''
Sample output
Enter price of item 1: 1.99
Enter price of item 2: 7.50
Enter price of item 3: 12.83
Enter price of item 4: 19.99
Enter price of item 5: 5.60
Subtotal of the sale: 47.91
Sales Tax: 3.35(7%)
Total to pay: 51.26'''

#While loop implementation
'''
QtyItems = int(input("How many items?: "))
i = 1
ttlPrice = 0
while i < (QtyItems+1):
    itemPrice = float(input("Enter item's price: "))
    ttlPrice = itemPrice + ttlPrice
    i+=1
salesTax = (ttlPrice * TAX_PRICE)
ttlPay = ttlPrice + salesTax
print(f"Subtotal of the sale: {ttlPrice:.2f} \nSales Tax: {salesTax:.2f}(7%) \nTotal to pay: {ttlPay:.2f}")
'''
'''
Sample output:
How many items?: 5
Enter item's price: 15
Enter item's price: 15
Enter item's price: 15
Enter item's price: 15
Enter item's price: 10
Subtotal of the sale: 70.00
Sales Tax: 4.90(7%)
Total to pay: 74.90
'''