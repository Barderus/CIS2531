'''
Author: Gabriel dos Reis
Date: 9/5/2023
Program: magicDate.py
Description: Design a program that asks the user to enter a month (in numeric form), 
a day, and a twodigit year. 
The program should then determine whether the month times the day equals the year. 
If so, it should display a message saying the date is magic. 
Otherwise, it should display a message saying the date is not magic.
'''

userDay = int(input("Enter a day: "))
userMonth = int(input("Enter a month: "))
userYear = int(input("Enter a year: "))

multiDayMonth = userDay * userMonth

if multiDayMonth == userYear:
    print("This date is magical!")
else:
    print("Nah, this date is not magical!")