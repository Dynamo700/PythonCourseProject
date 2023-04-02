import random
from db import get_money, write_money

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

    #print(card_deck)

    return card_deck

    #Use a list of lists to store the dealer's hand and the player's hand.

dealer_hand = []

player_hand = []

def play_game():
    money = get_money()
    if money < 5:
        print("Sorry. You don't have enough money to play right now.")
        answer = input("Would you like to buy some chips?")
        if answer.lower() == 'y':
            money = 100
            write_money(money)
        else:
            return

    deck = card_deck()
    player_selection = random.sample(deck, 2)
    player_hand.append(player_selection[0])
    player_hand.append(player_selection[1])

    #player selection. Remove cards from the deck
    deck.remove(player_selection[0])
    deck.remove(player_selection[1])
    print(len(deck))

    dealer_selection = random.sample(deck, 1)
    dealer_hand.append(dealer_selection[0])

    #Dealer selection. Remove cards from the deck
    deck.remove(dealer_selection[0])
    print(len(deck))

    for i in range(len(player_hand)):
        print(str(player_hand[i][1]) + " of " + player_hand [i][0])

    #Get user's input for the bet
    bet = input("Enter your bet amount (Min 5, Max 1000): ")
    bet = int(bet)
    while bet < 5 or bet > 1000:
        bet = input("Invalid bet amount. Bet must be higher than 5 and less than 1000.")
        bet = int(bet)
    money -= bet
    print(f"You just made a bet of: {bet}")
    print(f"You now have ${money} remaining.")
    write_money(money)





    #print(player_hand)

    #print(dealer_hand)


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

#card_deck()
display_title()
play_game()


    #NOTE: minimum bet of 5 and a maximum bet of 1000.






