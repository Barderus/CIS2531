'''
Author: Gabriel dos Reis
Date: 9/5/2023
Program: dayOfWeek.py
Description: Write a program that asks the user for a number in the range of 1 through 7.
The program should display the corresponding day of the week, where:
1 = Monday
2 = Tuesday
3 = Wednesday
4 = Thursday
5 = Friday
6 = Saturday
7 = Sunday. 
The program should display an error message if the user enters a number that is outside the range of 1 through 7.
'''

userChoice = int(input("Enter a number between 1 and 7: "))

if userChoice == 1:
    print("It's Monday!")
elif userChoice == 2:
    print("It's Tuesday!")
elif userChoice == 3:
    print("It's Wednesday!")
elif userChoice == 4:
    print("It's Thursday!")
elif userChoice == 5:
    print("It's Friday!")
elif userChoice == 6:
    print("It's Saturday!")
elif userChoice == 7:
    print("It's Sunday!")
else:
    print("Invalid number. Choose between 1 and 7.")