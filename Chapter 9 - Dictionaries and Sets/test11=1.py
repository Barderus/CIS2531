import random as r
ttl_cards = 0

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

def deal_cards(deck):
    hand = {}
    value_sum = 0
    for count in range(len(deck)):
        # Remove one card from the deck
        card, value = deck.popitem()
        # Add card to the hand
        hand[card] = value
        #print(hand[card])
        if hand[card] == 1 and value_sum <= 21:
            value_sum += 11
        else:
            value_sum += hand[card]   
        global ttl_cards
        ttl_cards += 1
        if value_sum >= 21:
            break
    print(value_sum)
    return hand

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
    shuffled_deck = dict(listDeck)
    
    print(deal_cards(shuffled_deck))
main()