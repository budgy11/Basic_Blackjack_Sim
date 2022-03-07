
def main():
    import deck
    import hand
    import chips

    play_deck = deck.Deck(6) #6 deck right now
    play_deck.shuffle()
    
    total_cards = play_deck.get_length()
    
    principal=100000
    player_chips = chips.Chips(principal)

    for i in range(0,10): 
        #print(i)
        reset_bet(player_chips) # resets bet to 0
        #Reshuffles deck after 70% penetrations
        if play_deck.get_length() < (0.3 * total_cards):
            play_deck = deck.Deck(6)
            play_deck.shuffle()

        player_hand = hand.Hand()
        player_hand.add_card(play_deck.deal())
        player_hand.add_card(play_deck.deal())
        
        dealer_hand = hand.Hand()
        dealer_hand.add_card(play_deck.deal()) 
        dealer_hand.add_card(play_deck.deal())
        
        dealer_card = dealer_hand.cards[1]

        betting(player_chips,10)
        hit_or_stand(play_deck,player_hand,dealer_card,player_chips,10)

        #this check should be done after but it creates a bug where for loop doesn't increment if after bust check
        if player_hand.value <= 21:
            while dealer_hand.value < 17: #currently stands on all 17
                hit(play_deck,dealer_hand)

        if player_hand.value > 21:
            player_busts(player_hand, dealer_hand, player_chips) 

        elif dealer_hand.value > 21: #
            dealer_busts(player_hand,dealer_hand,player_chips)

        elif dealer_hand.value > player_hand.value:
            dealer_wins(player_hand,dealer_hand,player_chips)

        elif dealer_hand.value < player_hand.value:
            player_wins(player_hand,dealer_hand,player_chips)

        else:
            push(player_hand,dealer_hand)

    print("\nPlayers winnings stand at", player_chips.total-principal)



def get_action(dealer_card,hand):
    from basic_strategy_tab import basic_strategy_hard
    from basic_strategy_tab import basic_strategy_soft

    if hand.aces == 0:
        return basic_strategy_hard[dealer_card][hand.value] #hand value passed into function
    else:
        return basic_strategy_soft[dealer_card][hand.value] #hand value passed into function

def reset_bet(chips):
    chips.bet = 0

def betting(chips, amt):
    if chips.total >= amt:
        chips.bet += amt #implement spread later
        #print(chips.bet)
    else:
        print("Sorry you're broke")
        exit()

def hit(deck,hand):
    hand.add_card(deck.deal())
    hand.adjust_for_ace()

def hit_or_stand(deck,hand,dealer_card,player_chips,amt):
    action = "X"
    while action != "S":
        if hand.value > 21:
            if hand.aces > 0:
                hand.adjust_for_ace()
            else:
                action = "S" #to prevent infinite looping
        elif get_action(dealer_card,hand) == "H":
            hit(deck,hand)
        elif get_action(dealer_card,hand) == "D":
            betting(player_chips,amt)
            hit(deck,hand)
            action = "S"
        elif get_action(dealer_card,hand) == "S": #might be unnecessary
            action = "S"
        else:
            print("error on choice")
            action = "S"


def player_busts(player,dealer_hand,chips):
    print("player busts")
    chips.lose_bet()

def player_wins(player,dealer,chips):
    print("player wins")
    chips.win_bet()

def dealer_busts(player,dealer,chips): # can probably remove and use player_wins
    print("dealer busts")
    chips.win_bet()

def dealer_wins(player,dealer,chips): # can probably use player_busts
    print("Dealer wins")
    chips.lose_bet()

def push(player,dealer):
    print("it's a tie")


if __name__ == "__main__":
    main()
