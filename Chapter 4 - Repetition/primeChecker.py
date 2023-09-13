'''
Author: Gabriel dos Reis
Date: 9/13/2023
Program: primeChecker.py
Description: Write a program that prompts the user for an integer and checks
if it's a prime number using a 'for' loop. A prime number is a positive integer greater
than 1 that has no positive divisors other than 1 and itself.
'''

# prompt user for a number to use on the checker
user_number = int(input("Enter a number: "))
if user_number > 1: # Prime numbers must be positive and bigger than 1
    for i in range(2, int(user_number/2)+1): #Iterates through a range of 2 to half of the number entered
        if (user_number % i) == 0:              # If the number can be divided by any number in the range it's not prime
            print(user_number, "is not a prime number")
            break #When the dividor is found, it stops and move to the second else statement
    else:
        print(user_number, "is a prime number") #If no divisor is found
else:
    print(user_number, "is not a prime number")
            