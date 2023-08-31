'''
Author: Gabriel dos Reis
Date: 8/31/2023
Description: Prompt user to enter total annual sales and display profit. 23% of profit.
'''
PROFIT_PERCENTAGE = 0.23
ttlSales = float(input("Enter annual total sales: "))
salesProfit = ttlSales * PROFIT_PERCENTAGE

print("This year total sales is: $", salesProfit)

