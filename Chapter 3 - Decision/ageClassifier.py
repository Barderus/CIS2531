'''
Author:
Date:
Program: ageClassifier.py
Description: Write a program that asks the user to enter a person’s age. 
The program should display a message indicating whether the person is an infant, 
a child, a teenager, or an adult. Following are the guidelines:
If the person is 1 year old or less, he or she is an infant.
                
If the person is older than 1 year, but younger than 13 years, he or she is a child.
                
If the person is at least 13 years old, but less than 20 years old, he or she is a teenager.
                
If the person is at least 20 years old, he or she is an adult.
'''
userChoice = int(input("Enter a person's age: "))

if userChoice < 1:
    print("This person is an infant!")
elif userChoice >= 1 and userChoice < 13:
    print("This person is a child!")
elif userChoice >= 13 and userChoice < 20:
    print("This person is a teenager!")
elif userChoice >= 20 and userChoice < 65:
    print("This person is an adult!")
else:
    print("This person is an elderly!")
