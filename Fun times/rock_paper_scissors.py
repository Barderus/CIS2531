'''
Author: Gabriel dos Reis
Date: 9/18/2023
Program: rock_paper_scissors.py
Description: Rock paper and scissors game
'''
import random
def main():
    print('Welcome to Rock Paper Scissors game!')
    get_user_choice()
    get_pc_choice()
    check_winner()
    display_result()
    sentinel = 1
    while play_again != "0":
        play_again = input("Would you like to play again? (Enter  to stop)")
        main()
    
    
def check_winner():
    print("We are checking the winner!")

def get_user_choice():
    print("We are checking your choice")
     
def get_pc_choice():
    print("We are checking the PC's choice!")
    
def display_result():
    print("We are displaying the result")
    
def store_result():
    print("We are storing the result")
    
main()