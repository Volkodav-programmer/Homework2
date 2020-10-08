class Card:

    Ranks=['T', '6', '7', '8', '9', '10', 'В', 'Д', 'К']
    Suits=[u'\u2660', u'\u2663', u'\u2665', u'\u2666']

    def __init__(self, rank, suit):
        self.rank=rank
        self.suit=suit

    def __str__(self):
        rep=self.rank+self.suit
        return rep

class Hand:
    def __init__(self):
        self.cards=[]

    def __str__(self):
        if self.cards:
            rep=''
            for card in self.cards:
                rep+=str(card) +'\t'
        else:
            rep='<Пусто>'
        return rep
    
    def clear(self):
        self.cards=[]

    def add(self, card):
        self.cards.append(card)

    def give(self, card, other_hand):
        self.cards.remove(card)
        other_hand.add(card)

class Deck(Hand):

    def populate(self):
        for suit in Card.Suits:
            for rank in Card.Ranks:
                self.add(Card(rank, suit))

    def shuffle(self):
        import random
        random.shuffle(self.cards)

    def deal(self, hands, per_hand=1):
        for rounds in range(per_hand):
            for hand in hands:
                if self.cards:
                    top_card=self.cards[0]
                    self.give(top_card, hand)
                else:
                    print('Карты закончились')
def main():
    print('Создаем колоду')
    deck_for_Durak=Deck()
    deck_for_Durak.populate()
    print('Колода создана')
    print('Тасуем карты')
    deck_for_Durak.shuffle()
    print('Колода готова')
    hand1=Hand()
    hand2=Hand()
    hand3=Hand()
    hand4=Hand()
    hands=[hand1, hand2, hand3, hand4]
    print('Время раздать карты')
    deck_for_Durak.deal(hands, per_hand=6)
    print('Карты розданы')
    print(hand1)
    print(hand2)
    print(hand3)
    print(hand4)

main()



