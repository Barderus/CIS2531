'''
Design a program that generates a seven-digit lottery number. 
The program should generate seven random numbers, each in the range of 0 through 9, and assign each number to a list element. 
(Random numbers were discussed in Chapter 5.) 
Then write another loop that displays the contents of the list.
'''
import random
def user_guess(lottery_list):
    # Initiate list to hold user's guess
    user_guess = []
    guess = 1

    # Loop to get user guesses
    while len(lottery_list) != len((user_guess)):
        user_guess.append(int(input(f"Enter your {guess} guess: ")))
        guess += 1
    return user_guess
    
def compare_numbers(lottery_list, user_guess):
        
    # Compare user input with the lottery ticket
    win = 0
    for n in range(0, len(lottery_list)):
        #i = 0
        if lottery_list[n] == user_guess[n]:
            win +=1
    return win
    
def main():
    # Initiate a list that holds the lottery list
    lottery_list = []
    
    # Populate the list
    for n in range(1,8):
        rand_num = random.randint(0,9)
        lottery_list.append(rand_num)
    
    # Function to get the user guess numbers
    guess = user_guess(lottery_list)
    #  Function to check how many numbers between the user_list and the lottery_list match
    win = compare_numbers(lottery_list, guess)
    
    # Print the lottery numbers
    print("You guessed: ", guess) 
    print("The lottery numbers are: ", lottery_list)
    
    # Print how much the user won
    if win == 7:
        print(f"You got {win} numbers right. You get all the price")
    elif win >= 5:
        print(f"You got {win} numbers right. You get 50% of the pize")
    else:
        print(f"You got {win} numbers right. You get no prize.")    
    
    
main()