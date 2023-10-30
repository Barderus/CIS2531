'''
Authir: Gabriel dos Reis
Date: 10/16/2023
Program: cardsDealer.py
Description: This program will deal cards to players from shuffled deck
    * The dictionary holds 13 cards of each suit, spades, hearts, clubs, diamonds
    * Randomly deal user specified number of cards from deck
        ** Remove card from deck
        ** Create user hand of cards
        ** Display user hand and calculate total value
'''

import random as r

def createDeck():
    # Create a dictionary of cards and its values
    # Stored as key-value pairs
    
    deckOfCards = {"Ace of Spades" : 1, "2 of Spades": 2, "3 of Spades": 3, "4 of Spades": 4, "5 of Spades": 5,
                   "6 of Spades": 6, "7 of Spades": 7, "8 of Spades": 8, "9 of Spades": 9, "10 of Spades": 10,
                   "Jack of Spades": 10, "Queen of Spades": 10, "King of Spades": 10,
                   
                   "Ace of hearts":1, "2 of hearts": 2, "3 of hearts": 3, "4 of hearts": 4, "5 of hearts": 5,
                   "6 of hearts": 6, "7 of hearts": 7, "8 of hearts": 8, "9 of hearts": 9, "10 of hearts": 10,
                   "Jack of hearts": 10, "Queen of hearts": 10, "King of hearts": 10,
                   
                   "Ace of clubs":1, "2 of clubs": 2, "3 of clubs": 3, "4 of clubs": 4, "5 of clubs": 5,
                   "6 of clubs": 6, "7 of clubs": 7, "8 of clubs": 8, "9 of clubs": 9, "10 of clubs": 10,
                   "Jack of clubs": 10, "Queen of clubs": 10, "King of clubs": 10,
                   
                   "Ace of diamonds":1, "2 of diamonds": 2, "3 of diamonds": 3, "4 of diamonds": 4, "5 of diamonds": 5,
                   "6 of diamonds": 6, "7 of diamonds": 7, "8 of diamonds": 8, "9 of diamonds": 9, "10 of diamonds": 10,
                   "Jack of diamonds": 10, "Queen of diamonds": 10, "King of diamonds": 10}
    return deckOfCards

# The dealCards function will take a deck and number of cards
# to deal and return a hand with the number of cards removed from the deck
def dealCards(deck, numCards):
    hand = {}
    
    # Verify the number of cards to deal
    # is not greater than the number of
    # cards in the deck
    
    if numCards > len(deck):
        print("Sorry, only", len(deck), "cards left in the deck")
        numCards = len(deck)
        
    # Deal the cards and accumulate the user hand
    
    for count in range(numCards):
        # Remove one card from the deck
        card, value = deck.popitem()
        # Add card to the hand
        hand[card] = value
        
    return hand

# The displayCards function will take a hand of cards
# As a dictionary and display the cards in the hand
# as well as the total value of the hand.
def displayHand(hand):
    handValue = 0
    
    # Iterate over each card in the hand
    for card,value in hand.items():
        # Display the card
        print("{:>20}".format(card))
        
        # Accumulate the value
        handValue += value
    # Display the hand value
    print("Value of this hand: ", handValue)    
        
def main():    
    # Create a deck of cards
    deck = createDeck()
    
    # Shuffle the deck
    # Convert dictionary of cards to list, shuffle list, convert back to dictionary
    listDeck = list(deck.items())
    
    # Using the random shuffle method to shuffle the list
    r.shuffle(listDeck)
    
    #Convert back to shuffled deck
    shuffledDeck = dict(listDeck)
    
    # Get number of cards to deal
    numCards = int(input("How many cards would you like? "))
    
    # Deal number of cards to a user's hand
    userHand = dealCards(shuffledDeck, numCards)
    
    # Display hand and calculate the value
    displayHand(userHand)
    
    
main()