import random
class Deck:
    def __init__(self, amt=1):
        self.deck = []
        for i in range(0,amt):
            for i in range(2,12): #add values for number cards and Aces
                for j in range(0,4):
                   self.deck.append(i) 
            for i in range(0,3): #add values for face cards K Q J
                for j in range(0,4):
                    self.deck.append(10)

    def __str__(self):
        deck_comp = ''
        for card in self.deck:
            deck_comp += '\n' + str(card)
        return deck_comp


    def shuffle(self):
        #self.deck = random.sample(self.deck,len(self.deck)) 
        random.shuffle(self.deck)

        


    def deal(self):
        return self.deck.pop()
    
    def get_list(self):
        return self.deck

    def get_length(self):
        return len(self.deck)
'''
deck = Deck(10)
print(deck.get_length())
deck.shuffle()

runs = 1000000
for i in range(0,runs):
    deck = Deck(10)
    deck.shuffle()
    print(deck.deal()) # output to file and cat | sort | uniq -c to count 

'''
