'''
Author:
Date:
Prorgram:
Description:
'''

# Importing random number functions

import random

#Named constants for "fair"
LOW_BOUND = 0.48
UP_BOUND = 0.52

def main():
    # Get the number of tosses from user
    num_tosses = int(input("Enter the number of coin tosses: "))
    # Keep track of number heads and tails
    number_heads = 0
    number_tails = 0
    
    # toss the coin
    for counter in range(0, num_tosses):
        # Generate random number
        rand_num = random.randint(1,2)
        # If the number is 1, it's heads
        if rand_num == 1:
            number_heads += 1
        # If the number is 2, it's tails
        else:
            number_tails += 1
    
    # See if the coin is fair
    if number_heads/num_tosses < LOW_BOUND or number_heads/num_tosses > UP_BOUND:
        print("The coin is not fair.")
    else:
        print("Hmmmm... May need to take a closer look at this coin.")
        
    # Print the results
    print("There were", format(number_heads/ num_tosses, ".2%"), "heads")
    print("There were", format(number_tails/ num_tosses, ".2%"), "tails")

# Call the main function
main()