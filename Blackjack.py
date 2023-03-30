import random


def display_title():
    print("BLACKJACK!")

    #Use a list for the suit, rank and point value

    #Use a list of lists to store the cards in the deck

def card_deck():

    suits = ["Spades", "Clubs", "Hearts", "Diamonds"]
    rank = ["Ace", 2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King"]
    point = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

    #Use a list of lists to store the cards in the deck
    card_deck = []

    for i in range(len(suits)):

        for j in range(len(rank)):
            card_deck.append([suits[i], rank[j], point[j]])

    random.shuffle(card_deck)

    print(card_deck)

    return card_deck

    #Use a list of lists to store the dealer's hand and the player's hand.

dealer_hand = []

player_hand = []


    # 1 spades
    # 2 spades
    # 3 spades
    # 4 spades
    # 5 spades
    # ......

    # 1 clubs
    # 2 clubs
    # 3 clubs
    # .....

card_deck()


    #NOTE: minimum bet of 5 and a maximum bet of 1000.






