import deck
class Hand:
    
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0

    def add_card(self,card):
        self.cards.append(card)
        #print(card)
        if card == 11:
            self.aces += 1
        if card == 'k' or card == 'q' or card == 'j':
            self.value += 10
        else:
            self.value += card

    def adjust_for_ace(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1
'''
for i in range(0,1000):
    import deck
    from basic_strategy_tab import basic_strategy_hard
    deck = deck.Deck()
    deck.shuffle()
    player = Hand()
    player.add_card(deck.deal())
    player.add_card(deck.deal())
    for dcard in player.cards:
        print(dcard,end=" ")
    print(player.value,end=" ")
    if player.value < 22:
        print(basic_strategy_hard[6][player.value])
    else:
        print("busted")
'''
