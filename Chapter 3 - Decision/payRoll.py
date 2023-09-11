'''
Author: Gabriel dos Reis
Date: 9/5/2023
Program: payRoll.py
Description: Example to use dual alternative in calculating overtime payroll
'''

# Named Constant
BASE_HOURS = 40
OT_MULTIPLIER = 1.5

# Get the user input
hoursWorked = int(input("Enter hours worked: "))
payRate = float(input("Enter pay rate value: "))

# Calculate gross pay
# Determine if overtime pay is calculated
if hoursWorked > BASE_HOURS:
    otHours = hoursWorked - BASE_HOURS
    otPay = otHours * payRate * OT_MULTIPLIER
    grossPay = BASE_HOURS * payRate + otPay
else:
    grossPay = hoursWorked * payRate
    
# Display the gross pay
print("Gross pay is $", format(grossPay, ",.2f"), sep=" ")

'''
### Sample output: ###
Enter hours worked: 40
Enter pay rate value: 13
Gross pay is $ 520.00
'''