'''
Author: Gabriel dos Reis
Date: 8/31/2023
Description: Write a program that calculates the total amount of a meal purchased at 
a restaurant. The program should ask the user to enter the charge for the food, 
then calculate the amounts of a 18 percent tip and 7 percent sales tax. 
Display each of these amounts and the total.
'''
SALES_TAX = 0.07
userCharge = float(input("Price of the meal: "))
userTip = int(input("How many percent of tip?: "))
tipCalc = userTip/100

taxPay = userCharge * SALES_TAX
ttlPay = userCharge + taxPay
tipAmnt = ttlPay * tipCalc

ttlAmnt = ttlPay + tipAmnt
print(f"The total meal price is {userCharge:.2f} \nSales tax:  {taxPay:.2f} \nTip amount:  {tipAmnt:.2f} \nTotal to pay: {ttlAmnt:.2f}")

'''
Sample output:
Price of the meal: 100
How many percent of tip?: 20
The total meal price is 100.00
Sales tax:  7.00
Tip amount:  21.40
Total to pay: 128.40'''