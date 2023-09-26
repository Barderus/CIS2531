'''
Author: Gabriel dos Reis
Date: 9/13/2023
Program: FibonacciSeq.py
Description: Write a program that displays the first 20 numbers in the Fibonacci sequence
The Fibonacci sequence starts with 0 and 1, 
and each subsequent number is the sum of the two preceding ones.
'''
INITIAL_NUMBER = 0
SECOND_NUMBER = 1

# Fibonacci number starts at 0
for x in range(10):
    print(INITIAL_NUMBER)
    sequence = INITIAL_NUMBER + SECOND_NUMBER # firstNum of the sequence + the second number
    INITIAL_NUMBER = SECOND_NUMBER # The first number now is the second number
    SECOND_NUMBER = sequence # The second number is sum of the previous sum