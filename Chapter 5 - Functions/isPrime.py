'''
Author: Gabriel dos Reis
Date: 9/19/2023
Program: prime_numbers.py
Description: Using a modular approach, prompt user for an integer limit and display all prime number from 2 to that number.
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
    user_number = int(input("Enter an integer limit: "))
    #Input validation
    while user_number < 2:
        print("Invalid input. Try again.")
        user_number = int(input("Enter an integer limit: "))
    print("The prime numbers in range of 2 to", user_number, "are: ")
    # Prints all the prime numbers up to the user's input
    count = 0
    for i in range(2, user_number + 1):
        if isPrime(i):
            print(i, end=" ")
            count += 1
    print()  
    print("There is a total of", count, "prime numbers.")

main()

# Output Sample
'''
Enter an integer limit: 100
The prime numbers in range of 2 to 100 are:
2 3 5 7 11 13 17 19 23 29 31 37 41 43 47 53 59 61 67 71 73 79 83 89 97
There is a total of 25 prime numbers.
'''