import random
class Card:
    
    suit_card = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    value_card = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    
    def __init__(self, suit, value):
        if suit not in Card.suit_card or value not in Card.value_card:
            raise ValueError
        self.suit = suit
        self.value = value
    
    def __repr__(self):
        return self.value + ' of '+ self.suit



class Deck:

    def __init__(self):
        suit  = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        value = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        self.cards = [Card(s,v) for v in value for s in suit ]

    def count(self):
        return len(self.cards)

    def _deal(self, num):

        if num > len(self.cards):
            num = len(self.cards)
        if len(self.cards) == 0:
            raise ValueError("All cards have been dealt")
        else:
            deal_card = self.cards[-num:]
            self.cards = self.cards[0:-num]
            return deal_card

    def shuffle(self):
        if len(self.cards) != 52:
            raise ValueError("Only full decks can be shuffled")
        return random.shuffle(self.cards)

    def deal_card(self):
        return self._deal(1)[0]

    def deal_hand(self,num):
        return self._deal(num)

    def __repr__(self):
        # for w in self.cards:
        #     print(w)
        # print(self.cards[0].suit)
        return 'Deck of '+ str(len(self.cards)) +' cards'


my_deck = Deck()
print(my_deck)
my_deck.shuffle()
card = my_deck.deal_card()
print(card)
hand = my_deck.deal_hand(5)
print(hand)
print(my_deck)