import random

def deal_cards(deck, player_hand, dealer_hand):
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