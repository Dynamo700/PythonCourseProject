import random
from db import get_money, write_money
from deal import deal_cards
from reset import reset_hands

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

    return card_deck

    #Use a list of lists to store the dealer's hand and the player's hand.


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

def play_game():
    #If the money in money.txt is below the minimum bet of 5, ask if the player would like to buy chips

    money = get_money()

    get_bet(money)

    deck = card_deck()

    deal_cards(deck, player_hand, dealer_hand)


    print("DEALER'S SHOW CARD: ")
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
                card = card_selection[0]
                if card[2] == 11:
                    #Ask player if they want the ace to be a 1 or an 11
                    print("You drew an ace! What would you like it to be?")
                    while True:
                        try:
                            ace_selection = int(input("1 or 11?"))
                            if ace_selection in [1, 11]:
                                card = (card[0], card[1], ace_selection)
                                break
                            else:
                                print("Invalid input. Please enter either a 1 or an 11.")
                        except ValueError:
                            print("Invalid input. Please enter either a 1 or an 11.")
                    #If an 11 would make the user's hand value go over 21, automatically set it to 1.
                    if sum([a[2] for a in player_hand]) + card[2] > 21:
                        card_selection = (card[0], card[1], 1)
                player_hand.append(card_selection[0])
                deck.remove(card_selection[0])
                print()
                print("YOUR CARDS: ")
                #Select a card for the player
                for i in range(len(player_hand)):
                    print(str(player_hand[i][1]) + " of " + player_hand[i][0])
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
        print("DEALER'S CARDS: ")
        for i in range(len(dealer_hand)):
            print(str(dealer_hand[i][1]) + " of " + dealer_hand[i][0])
        dealers_total = sum([card[2] for card in dealer_hand])

    determine_results(dealer_hand, player_hand, money)

#Determine who won. If the player wins, award the payout to the money.txt file
def determine_results(dealer_hand, player_hand, money):
    if sum([card[2] for card in player_hand]) > 21:
        money -= bet
        print()
        print("Sorry. You lose.")
        write_money(money)
        print(f"money: {money:.2f}")
    elif sum([card[2] for card in dealer_hand]) > 21:
        money += bet * 1.5
        print()
        print("Well done! you win!")
        write_money(money)
        print(f"money: {money:.2f}")
    elif sum([card[2] for card in dealer_hand]) > sum([card[2] for card in player_hand]):
        money -= bet
        print()
        print("Sorry. You lose.")
        write_money(money)
        print(f"money: {money:.2f}")
    elif sum([card[2] for card in player_hand]) > sum([card[2] for card in dealer_hand]):
        money += bet * 1.5
        print()
        print("Well done! you win!")
        write_money(money)
        print(f"money: {money:.2f}")


def display_hand_points(dealer_hand, player_hand):
    #Determine score
    dealer_score = sum([card[2] for card in dealer_hand])
    player_score = sum([card[2] for card in player_hand])
    print()
    print(f"YOUR POINTS: {player_score}")
    print(f"DEALER'S POINTS: {dealer_score}")

def main():
    display_title()
    play_game()
    display_hand_points(dealer_hand, player_hand)

    play_again = "y"
    while play_again.lower() == "y":
        print()
        play_again = input("Play again? (y/n)")
        if play_again.lower() == "y":
            reset_hands(player_hand, dealer_hand)
            play_game()
            display_hand_points(dealer_hand, player_hand)

    print()
    print("Come back soon!")
    print("Bye!")

if __name__ == "__main__":
    main()