'''
Author: Gabriel dos Reis
Date: 9/18/2023
Program: rock_paper_scissors.py
Description: Rock paper and scissors game
'''
import random
ROCK = 1
PAPER = 2
SCISSORS = 3
EXIT = -1

def display_menu():
    print("Rock Paper Scissors Game")
    print("---------")
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors") 
    print("4. Quit")
    print()

def get_user_choice(choice):
        if choice == ROCK:
            print("You chose Rock!")
            return ROCK
        elif choice == PAPER:
            print("You chose Paper!")
            return PAPER
        elif choice == SCISSORS:
            print("You chose Scissors!")
            return SCISSORS
        elif choice == EXIT:
            print("Terminating program...")
            exit()
        else:
            print("Error! You must enter a number between 1 and 3.")
            choice = int(input("Choose between 1(Rock), 2(Paper) or 3(Scissors): (-1 to exit game):"))

def get_user_choice(choice):
        if choice == ROCK:
            print("You chose Rock!")
            return ROCK
        elif choice == PAPER:
            print("You chose Paper!")
            return PAPER
        elif choice == SCISSORS:
            print("You chose Scissors!")
            return SCISSORS
        elif choice == EXIT:
            print("Terminating program...")
            exit()
        else:
            print("Error! You must enter a number between 1 and 3.")
            choice = int(input("Choose between 1(Rock), 2(Paper) or 3(Scissors): (-1 to exit game):"))
      
def check_winner(player_choice, pc_choice):
    if player_choice == pc_choice:
        print("It's a tie!")
    elif player_choice == ROCK:
        if pc_choice == SCISSORS:
            print("Rock smashes scissors! You win!")
        else:
            print("Paper covers rock! You lose.")
    elif player_choice == PAPER:
        if pc_choice == ROCK:
            print("Paper covers rock! You win!")
        else:
            print("Scissors cut paper! You lose.")
    elif player_choice == SCISSORS:
        if pc_choice == PAPER:
            print("Scissors cut paper! You win!")
        else:
            print("Rock smashes scissors! You lose.")

 
def get_pc_choice():
    pc_random = random.randint(1,3)
    print("PC random number:", pc_random)
    if pc_random == ROCK:
        print("PC chose Rock")
    elif pc_random == PAPER:
        print("PC chose Paper")
    elif pc_random == SCISSORS:
        print("PC chose Scissors")
    
def display_result():
    print("We are displaying the result")
    
def store_result():
    print("We are storing the result")
    
def main():
    player_input = int(input("Choose between 1(Rock), 2(Paper) or 3(Scissors): (-1 to exit game): "))
    player_choice = get_user_choice(player_input)
    pc_choice = get_pc_choice()
    check_winner(player_choice, pc_choice)
    display_result() 
    
main()