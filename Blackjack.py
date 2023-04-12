import random
from db import get_money, write_money

dealer_hand = []

player_hand = []

bet = 0

def display_title():
    print("BLACKJACK!")
    print("Blackjack payout is 3:2")

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

    #Reset the player and dealer hands if the player selects "y" when asked if they want to play again
def reset_hands():
    dealer_hand.clear()
    player_hand.clear()


def get_bet(money):
    print()
    print(f"Money: {money:.1f}")
    while True:
        global bet
        #Get the bet amount from the player
        bet = input("Bet amount: ")
        print()
        try:
            bet = int(bet)
            if bet < 5 or bet > 1000:
                #Make sure that the user can't make a bet greater than 1000 or less than 5.
                raise ValueError("Invalid bet amount. Bet must be higher than 5 and less than 1000.")
        except ValueError as e:
            print(e)
        else:
            #Make sure that the user can't make a bet that is greater than the money in the money.txt
            if bet > money:
                print("Sorry, you don't have enough money to make that bet. Please try again.")
            else:
                money -= bet
                write_money(money)
                break


def deal_cards(deck):
    card_selection = random.sample(deck, 2)
    player_hand.append(card_selection[0])
    player_hand.append(card_selection[1])

    #player selection. Remove cards from the deck
    deck.remove(card_selection[0])
    deck.remove(card_selection[1])

    dealer_selection = random.sample(deck, 1)
    dealer_hand.append(dealer_selection[0])

    #Dealer selection. Remove cards from the deck
    deck.remove(dealer_selection[0])

def play_game():
    #If the money in money.txt is below the minimum bet of 5, ask if the player would like to buy chips

    money = get_money()

    get_bet(money)

    deck = card_deck()

    deal_cards(deck)


    print("DEALER SHOW CARD: ")
    print(str(dealer_hand[0][1]) + " of " + dealer_hand[0][0])

    print()
    print("YOUR CARDS: ")
    for i in range(len(player_hand)):
        print(str(player_hand[i][1]) + " of " + player_hand[i][0])


    #Get user's input for the bet
    #Player's turn
    while True:
        try:
            print()
            choice = input("Hit or stand? (hit/stand): ")
            if choice.lower() == "hit":
                card_selection = random.sample(deck, 1)
                player_hand.append(card_selection[0])
                deck.remove(card_selection[0])
                print()
                print("YOUR CARDS: ")
                #Select a card for the player
                for i in range(len(player_hand)):
                    print(str(player_hand[i][1]) + " of " + player_hand[i][0])
                if sum([card[2] for card in player_hand]) > 21:
                    print()
                    print("Sorry. You lose.")
                    write_money(money)
                    print(f"Money: {money:.1f}")
                    return
            elif choice.lower() == "stand":
                break
            else:
                print("Invalid input. Please enter either hit or stand.")
        except:
            print("Invalid input. Please enter either hit or stand.")

    #Dealer's turn
    dealers_total = sum([card[2] for card in dealer_hand])
    while dealers_total < 17:
        #Pick a random card from the deck, add it to the dealer's hand and than remove it from the deck.
        card_selection = random.sample(deck, 1)
        dealer_hand.append(card_selection[0])
        deck.remove(card_selection[0])
        print()
        print("DEALER CARDS: ")
        for i in range(len(dealer_hand)):
            print(str(dealer_hand[i][1]) + " of " + dealer_hand[i][0])


        if sum([card[2] for card in dealer_hand]) > 21:
            money += bet * 1.5
            print()
            print("The dealer has busted! you win!")
            write_money(money)
            print(f"money: {money:.1f}")
            return

#Determine who won. If the player wins, award the payout to the money.txt file
def determine_results(dealer_hand, player_hand, money):

    display_hand_points(dealer_hand, player_hand)

    if sum([card[2] for card in dealer_hand]) > sum([card[2] for card in player_hand]):
        money -= bet
        print("Sorry. You lose.")
        print(money)
        print()
    elif sum([card[2] for card in dealer_hand]) == sum([card[2] for card in player_hand]):
        money -= bet
        print("Tie!")
        print(money)
        print()
    else:
        money += bet * 1.5
        print()
        print("Well done! you win!")
        write_money(money)
        print(f"money: {money:.1f}")

def display_hand_points(dealer_hand, player_hand):
    #Determine score
    dealer_score = sum([card[2] for card in dealer_hand])
    player_score = sum([card[2] for card in player_hand])
    print()
    print(f"YOUR POINTS: {player_score}")
    print(f"DEALER POINTS: {dealer_score}")

def main():
    display_title()
    play_game()
    display_hand_points(dealer_hand, player_hand)

    play_again = "y"
    while play_again.lower() == "y":
        print()
        play_again = input("Play again? (y/n)")
        if play_again.lower() == "y":
            reset_hands()
            play_game()
            display_hand_points(dealer_hand, player_hand)

    print()
    print("Come back soon!")
    print("Bye!")

if __name__ == "__main__":
    main()