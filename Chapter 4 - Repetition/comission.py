'''
Author: Gabriel dos Reis
Date: 9 / 11 / 2023
Program: comission.py
Description: Follow along program that calculates the comission of a sale. It uses while loop
to prompt if user wants  to calculate another comission.
'''

# Sentinel
keep_going = "y"

while keep_going:
    sales = float(input("Enter the amount of sales: "))
    commisionRate = float(input("Enter the comission rate: "))
    
    #Calculate comission
    comission = sales * commisionRate
    
    #Display
    print(f"The comission is ${comission:.2f}.")
    
    #Check if user wants to do another one
    keep_going = input("Do you want to calculate another comission? (Enter y for yes: )")
    
