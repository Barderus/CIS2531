'''
Author: Gabriel dos Reis
Date: 10/18/2023
program: blackjack.py
Description:

Requiriments:
    * Play one round of the game (Deal cards from deck for each player's hand until winner for the round)
        ** Each hand is a dictionary with corresponding key-value items removed from the dictionary deck
    * Deal cards until one player hand is worth 21 or more points OR there are no more cards in the deck
    * Winner = Closest or equal 21 but not over it
    * Calculate the value of each hand
    * Use a batch mode approach without player intervention until all cards have been played
    * Ace = 11 points, but after 21 it is worth 1 point
    * Column headers to organize output for each round
    * At the end of the game, print summary game statistics
    Sample output:
    --> ** NEW ROUND **
        Deal        Player1         Player2
        ----        -------         -------
        1           2 of Hearts     3 of Spades
        2           4 of Diamonds   5 of Clubs
        3           6 of Hearts     7 of Spades
    ================================    ========
    Hand value:     12                      15
    Player2 wins.
    
    ** SUMMARY GAME STATISTICS **
    Round player
    Cards played
    Player 1 wins
    Player 2 wins
    Both wins
    No wins
    
    # Play until all cards are dealt. If there are no more cards in the deck, the game is over.
        At the end of each round shows which player won.
'''

import random as r

def createDeck():
    # Create a dictionary of cards and its values
    # Stored as key-value pairs
    
    deckOfCards = {"Ace of spades" : 1, "2 of spades": 2, "3 of spades": 3, "4 of spades": 4, "5 of spades": 5,
                   "6 of spades": 6, "7 of spades": 7, "8 of spades": 8, "9 of spades": 9, "10 of spades": 10,
                   "Jack of spades": 10, "Queen of spades": 10, "King of spades": 10,
                   
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
def dealCards(deck, num_cards):
    hand = {}
    for _ in range(num_cards):
        if not deck:
            print("The deck is empty.")
            break
        card, value = deck.popitem()
        hand[card] = value
    return hand


# The displayCards function will take a hand of cards
# As a dictionary and display the cards in the hand
# as well as the total value of the hand.
def displayHand(player_hand, player_name):
    print(f"    --> ** NEW ROUND **")
    print(f"    Deal        Player1         Player2")
    print(f"    ----        -------         -------")
    if isinstance(player_hand, dict):
        player_value = sum(player_hand.values())
        print(f"{player_name}'s hand:")
        for card, value in player_hand.items():
            print(f"{card}: {value}")
        print(f"{player_name}'s hand value: {player_value}")
        return player_value
    else:
        print(f"{player_name}'s hand is empty.")
        return 0
    
def playRound(deck, player1_wins, player2_wins, rounds_played):
    rounds_played += 1
    print(f"Round {rounds_played} - Dealing cards...")

    # Shuffle the deck
    listDeck = list(deck.items())
    r.shuffle(listDeck)
    shuffledDeck = dict(listDeck)

    # Deal cards to both players
    player1_hand = dealCards(shuffledDeck, 2)
    player2_hand = dealCards(shuffledDeck, 2)

    # Display each player's hand and calculate the value
    player1_value = displayHand(player1_hand, "Player 1")
    player2_value = displayHand(player2_hand, "Player 2")

    # Determine the winner of the round
    if player1_value > 21 and player2_value <= 21:
        print("Player 2 wins this round!")
        player2_wins += 1
    elif player2_value > 21 and player1_value <= 21:
        print("Player 1 wins this round!")
        player1_wins += 1
    elif player1_value <= 21 and player2_value <= 21:
        if player1_value > player2_value:
            print("Player 1 wins this round!")
            player1_wins += 1
        elif player2_value > player1_value:
            print("Player 2 wins this round!")
            player2_wins += 1
        else:
            print("It's a tie in this round!")
    print()

    # Return updated deck
    return player1_wins, player2_wins, rounds_played, shuffledDeck

def main():
    player1_wins = 0
    player2_wins = 0
    rounds_played = 0

    # Create a deck of cards
    deck = createDeck()

    while deck:
        player1_wins, player2_wins, rounds_played, deck = playRound(deck, player1_wins, player2_wins, rounds_played)

    print("\nGame Over!")
    print(f"Player 1 wins: {player1_wins} rounds")
    print(f"Player 2 wins: {player2_wins} rounds")
    print(f"Total rounds played: {rounds_played}")

if __name__ == "__main__":
    main()
    
'''
    Sample output:
    --> ** NEW ROUND **
        Deal        Player1         Player2
        ----        -------         -------
        1           2 of Hearts     3 of Spades
        2           4 of Diamonds   5 of Clubs
        3           6 of Hearts     7 of Spades
    ================================    ========
    Hand value:     12                      15
    Player2 wins.
    
    ** SUMMARY GAME STATISTICS **
    Round player
    Cards played
    Player 1 wins
    Player 2 wins
    Both wins
    No wins'''