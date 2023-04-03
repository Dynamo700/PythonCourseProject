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

#Calculate the amount of points
def points(hand):
    points_total = 0
    aces = 0
    for card in hand:
        points_total += card[2]
        if card[1] == 'Ace':
            aces += 1
    while aces > 0 and points_total > 21:
        points_total -= 6
        aces -= 1
    return points_total


def play_game():
    money = get_money()
    if money < 5:
        print("Sorry. You don't have enough money to play right now.")
        answer = input("Would you like to buy some chips? (y/n)")
        if answer.lower() == 'y':
            money = 100
            write_money(money)
        else:
            return

    deck = card_deck()
    card_selection = random.sample(deck, 2)
    player_hand.append(card_selection[0])
    player_hand.append(card_selection[1])

    #player selection. Remove cards from the deck
    deck.remove(card_selection[0])
    deck.remove(card_selection[1])
    print(len(deck))

    dealer_selection = random.sample(deck, 1)
    dealer_hand.append(dealer_selection[0])

    #Dealer selection. Remove cards from the deck
    deck.remove(dealer_selection[0])
    print(len(deck))

    print("Your cards: ")
    for i in range(len(player_hand)):
        print(str(player_hand[i][1]) + " of " + player_hand[i][0])
        print()

    print("Dealer's cards: ")
    print(str(dealer_hand[0][1]) + " of " + dealer_hand[0][0])
    print()

    # Get user's input for the bet
    bet = input("Enter your bet amount (Min 5, Max 1000): ")
    bet = int(bet)
    while bet < 5 or bet > 1000:
        bet = input("Invalid bet amount. Bet must be higher than 5 and less than 1000.")
        bet = int(bet)
    money -= bet
    print(f"You just made a bet of: {bet}")
    print(f"You now have ${money} remaining.")
    write_money(money)

    #Player's turn
    while True:
        choice = input("Hit or stand? (hit/stand): ")
        if choice.lower() == "hit":
            card_selection = random.sample(deck, 1)
            player_hand.append(card_selection[0])
            deck.remove(card_selection[0])
            print("Your cards are: ")
            for i in range(len(player_hand)):
                print(str(player_hand[i][1]) + " of " + player_hand[i][0])
            if sum([card[2] for card in player_hand]) > 21:
                print("Sorry. You lose.")
                write_money(money)
                return
        else:
            break

    #Dealer's turn
    dealers_total = sum([card[2] for card in dealer_hand])
    while dealers_total < 17:
        card_selection = random.sample(deck, 1)
        dealer_hand.append(card_selection[0])
        deck.remove(card_selection[0])
        print("The dealer's cards are as follows: ")
        for i in range(len(dealer_hand)):
            print(str(dealer_hand[i][1]) + " of " + dealer_hand[i][0])
        if sum([card[2] for card in dealer_hand]) > 21:
            money += bet * 1.5
            print("Well done! you win!")
            print("Here's your payout.")
            write_money(money)
            return

    #Determine Results
    if sum([card[2] for card in dealer_hand]) > sum([card[2] for card in player_hand]):
        print("Sorry. You lose.")
        print(money)
        print()
    elif sum([card[2] for card in dealer_hand]) == sum([card[2] for card in player_hand]):
        print("Tie!")
        print(money)
        print()
    else:
        money += bet * 1.5
        print("Well done! you win!")
        print("Here's your payout.")
        write_money(money)


        #Update the dealer's total

        dealers_total = sum([card[2] for card in dealer_hand])












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






