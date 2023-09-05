'''
Author: Gabriel dos Reis
Date: 8/31/2023
Description: Last month, Joe purchased some stock in Acme Software, Inc
The details of the purchase:
    Number of share that Joe purchased: 2,000
    When Joe purchased the stock: $40.00 per share
    Joe paid his stockbroker a commission that amounted to 3% of the 
    amount he paid for the stock.
Two weeks later he sold the stock. Here are the details of the sale:
    Number of shares that Joe sold: 2,000
    He sold the stock for: $42.75 per share
    He paid his stockbroker another commission that amounted to 3% of 
    the amount he received for the stock
Write a program that displays the following information:
    The amount of money Joe paid for the stock
    The amount of commission Joe paid his broker when he bought the stock
    The amount that Joe sold the stock for
    The amount of commission Joe paid his broker when he sold the stock
    Display the amount of money that Joe had left when he sold the stock
    and paid his broker (both times). If this amount is positive, then
    Joe made a profit. If the amount is negative, then Joe lost money.
'''

# Constants
COMMISSION_RATE = 0.03

# Variables
sharesPurch = 2000
sharesPrice = 40.00
sharesSold = 2000
sharesSoldPrice = 42.75

# Calculations
amntPaid = sharesPurch * sharesPrice
commPaid = amntPaid * COMMISSION_RATE
amntSold = sharesSold * sharesSoldPrice
commSold = amntSold * COMMISSION_RATE
amntLeft = amntSold - commSold - amntPaid - commPaid

# Display
print(f"Joe paid ${amntPaid:.2f} for the stock. \nJoe paid ${commPaid:.2f} in comission to his broker. \nJoe sold the stocks for ${amntSold:.2f}. \nJoe paid ${commSold:.2f} in comission to his broker. \nJoe had ${amntLeft:.2f} left after selling the stocks and paying his broker.")

# Output
'''
Joe paid $80000.00 for the stock. 
Joe paid $2400.00 in comission to his broker.
Joe sold the stocks for $85500.00.
Joe paid $2565.00 in comission to his broker.
Joe had $535.00 left after selling the stocks and paying his broker.
'''
