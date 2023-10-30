'''
Author: Gabriel dos Reis
Date: 10/25/2023
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
    * Play until all cards are dealt. If there are no more cards in the deck, the game is over.
        At the end of each round shows which player won.
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
    
'''
import random as r

# Initiaize a global variable to store cards dealt
ttl_cards = 0

def createDeck():
    '''
    Create a dictionary of cards and its values stored as key-value pairs 
    '''
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


def deal_cards(deck):
    '''
    Function that receives a shuffled deck and deal cards to the players_hand until they reach the hand value of 21 or more.
        This function also keeps track of the amount of cards dealt.
        Also, this function changes the value of the Aces from 1 to 11 if the value of hand is under 21. 
    '''
    hand = {}
    value_sum = 0
    for count in range(len(deck)):
        # Remove one card from the deck
        card, value = deck.popitem()
        # Add card to the hand
        hand[card] = value
        # If the card is an Ace and the value of the hand is less than 21, change the value of the key to 11
        if hand[card] == 1 and value_sum <= 21:
            hand[card] = 11
        value_sum += hand[card]
        # Initialize the global variable ttl_cards to store the amount of cards dealt
        global ttl_cards
        ttl_cards += 1
        # Condition to stop dealing cards once the player hand reaches to 21 or more
        if value_sum >= 21:
            break
    return hand
    
def display_hand(player1_hand, player2_hand, round):
    '''
    This function receives as an argument the dictionary player1_hand, dictionary player2_hand, and round.
        Then it uses the data from these variables to display the information into the table.
    '''
    # Table header
    print(f"\n    --> ** ROUND {round} **")
    print("    Deal        Player1         Player2")
    print("    ====        =======         =======")
    
    # Initialize variable to hand the hand value of each hand and how many cards were dealt
    handValue = 0
    hand2Value = 0
    deal = 1
   
    # Iterate over both hands simultaneously using zip()
    for (card1, value1), (card2, value2) in zip(player1_hand.items(), player2_hand.items()):
        # Display the cards of both players in the same line
        print(f"{deal:>5} {card1:>20} {card2:>20}")

        # Accumulate the values for both hands
        handValue += value1
        hand2Value += value2
        deal += 1
 
def play_round(shuffled_deck, player1_wins, player2_wins, players_win, no_win, rounds_played):
    rounds_played += 1
    '''
    This function takes a shuffle deck, player1_wins, player2_wins, player_win, no_win, rounds_played as an argument
        Shuffled deck -> dictinary with the all the 52 cards shuffled
        player1_wins -> An integer variable to acumulate the number of times player1 has won
        player2_wins -> An integer variable to acumulate the number of times player2 has won
        players_win -> An integer variable to acumulate the number of times both players won
        no_win -> An integer variable to acumulate the number of times no player won
        rounds_played -> An integer variable to acumulate the number of rounds played
        
        This function also display the hand value of each player and checks who won the round, then it returns
            player1_wins, player2_wins, players_win, no_wins, and rounds_played.
    '''
    # Call the function deal_cards to deal cards to each player's hand
    player1_hand = deal_cards(shuffled_deck)
    player2_hand = deal_cards(shuffled_deck)
    
    # Call the function to display the hand of each player
    display_hand(player1_hand, player2_hand, rounds_played)
    
    # Calculate player hand values
    player1_value = sum(player1_hand.values())
    player2_value = sum(player2_hand.values())

    # Display the hand value of each player
    print("==================================================")
    print(f"Hand value: {player1_value:^20}{player2_value:^20}\n")
    
    # Determine the winner of the round
    '''
    If player 1 hand value is 21 or less than 21 when player 2 hand value is more than 21, then player 1 wins
        If both player 1 and 2 hand value are less than 21, but player 1 hand value is higher than player 2 value, then player 1 wins
    If player 2 hand value is 21 or less than 21 when player 1 hand value is more than 21, then player 2 wins
            If both player 1 and 2 hand value are less than 21, but player 2 hand value is higher than player 1 value, then player 2 wins
    If both players hand value is over 21, then both players lost
    If both players hand value is equal to 21, then both players win
    '''
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
    elif player1_value == 21 and player2_value == 21:
        print("Both player win!")
        players_win += 1
    else:
        print("No one wins")
        no_win += 1
    
    # Return updated deck
    return player1_wins, player2_wins, players_win, no_win, rounds_played

            
def main():
    '''
    Main function that creates the deck of cards and shuffle it, then call the function play_round until there are cards available to be dealt
        then, after all cards are dealt, display the game statistics displaying:
           * how many rounds were played
           * how many cards were plyed
           * how many rounds player 1 won
           * how many rounds player 2 won
           * how many rounds both players won
           * how many rounds neither player won
    '''
    player1_wins = 0
    player2_wins = 0
    players_win = 0
    no_win = 0
    rounds_played = 0

    # Create a deck of cards
    deck = createDeck()
    
    # Shuffle the deck
    # Convert dictionary of cards to list, shuffle list, convert back to dictionary
    listDeck = list(deck.items())
    
    # Using the random shuffle method to shuffle the list
    r.shuffle(listDeck)
    
    #Convert back to shuffled deck
    shuffled_deck = dict(listDeck)
    
    # While the shuffled deck isn't empty
    while shuffled_deck:
        player1_wins, player2_wins,players_win, no_win, rounds_played = play_round(shuffled_deck, player1_wins, player2_wins, players_win, no_win, rounds_played) 
    
    # Display the game's statistics           
    print("\n\t** SUMMARY GAME STATISTICS **")
    print(f"Rounds played: {rounds_played}")
    print(f"Cards played: {ttl_cards}")
    print(f"Player 1 wins: {player1_wins} rounds")
    print(f"Player 2 wins: {player2_wins} rounds")
    print(f"Both wins: {players_win}")
    print(f"No one wins: {no_win}")

# Call the main function 
if __name__ == "__main__":
    main()