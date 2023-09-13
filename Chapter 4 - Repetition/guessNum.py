'''
Author: Gabriel dos Reis
Date: 9/13/2023
Program: guessNumber.py
Description: Create a simple 'Guess the Number' game
where the computer slects a random number between 1 and 100, and the user has to guess it.
Provide feedback to the user after each guess, indicating if the guessed number is
too high or too low.
Use a 'while' loop to keep the game running until the user correctly
guesses the number.
'''
import random

random_int = random.randint(1,100) 
print(random_int)

while True:
    user_guess = int(input("Enter your number: "))
    
    if user_guess < random_int:
        print("You guessed too low!")
    elif user_guess > random_int:
        print("You guessed too high!")
    else:
        print("Din din! You guessed it right!")
        break
    
