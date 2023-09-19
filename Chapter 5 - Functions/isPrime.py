'''
Author: Gabriel dos Reis
Date: 9/19/2023
Program: prime_numbers.py
Description:
'''

def isPrime(int_num):
    ''' This function takes an integer and returns True if it is prime and False if it is not.'''
    if int_num == 2:
        return True
    if int_num % 2 == 0:
        return False
    # Checks if the number is divisible by any odd number up to its square root
    for i in range(3, int_num, 2):
        if int_num % i == 0:
            return False
    return True
    
def main():
    ''' This function takes an integer from the user and prints all the prime numbers up to that integer.'''
    user_number = int(input("Enter an integer limit:"))
    #Input validation
    while user_number < 2:
        print("Invalid input. Try again.")
        user_number = int(input("Enter an integer limit:"))
    # Prints all the prime numbers up to the user's input
    for i in range(2, user_number + 1):
        if isPrime(i):
            print(i, end=" ")

main()