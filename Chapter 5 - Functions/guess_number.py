'''
Guess the number game '''

import random

def random_num():
    return random.randint(1,100)


def main():
    print("Welcome to Guess the number game! \nYou have 4 chances to guess a number between 1 and a 100")
    
    while True:
        number_guess = random_num()
        print(number_guess)
        win = 0
        chances = 0
        for g in range(4):
            player_guess = int(input("Enter a number between 1 and 100 (-1 to quit): "))
            if player_guess == -1:
                print("Quitting the game...")
                return
            if player_guess < number_guess:
                print("You guessed too low!")
            elif player_guess > number_guess:
                print("You guessed too high!")
            elif player_guess == number_guess:
                win += 1
                print("JACKPOT! You guessed the right number!")
                print("Starting a new game...")
                print()
                break
            chances += 1
            print("You have", (4 - chances), "left")
            print()
        print("You have won", win, "times so far.")
        print()


main()
