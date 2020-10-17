import random
import cards
import games
from tkinter import *
class BJ_Table:
     root = Tk()
     root.title("black_jack_table")
     c = Canvas(root, width=1000,height=1000, bg="gray")
     c.pack()
     c.create_polygon(50, 150, 200, 700, 800, 700, 950, 150, fill='dark green', outline='black', width=2)
     c.create_rectangle(375, 250, 410, 300, fill='white', outline='black', width=2)
     c.create_rectangle(435, 250, 470, 300, fill='white', outline='black', width=2)
     c.create_rectangle(495, 250, 530, 300, fill='white', outline='black', width=2)
     c.create_rectangle(555, 250, 590, 300, fill='white', outline='black', width=2)
     c.create_rectangle(615, 250, 650, 300, fill='white', outline='black', width=2)
class BJ_Card(cards.Positionable_card):
    ACE_VALUE = 1

    @property
    def value(self):
        if self.is_face_up:
            v = BJ_Card.RANKS.index(self.rank) + 1
            if v > 10:
                v = 10
        else:
            v = None
        return v

class BJ_Deck(cards.Deck):
    """  Колода для игры в Блек-джек. """
    def populate(self):
        for suit in BJ_Card.SUITS:
            for rank in BJ_Card.RANKS:
                self.cards.append(BJ_Card(rank, suit))

class BJ_Hand(cards.Hand):
    ''' Рука игрока в Блек-джек. ''' 
    def __init__(self, name):
        super().__init__()
        self.name = name

    @property
    def total(self):
        for card in self.cards:
            if not card.value:
                return None
        t = 0
        contains_ace = False
        for card in self.cards:
            t += card.value
            if card.value == BJ_Card.ACE_VALUE:
                contains_ace = True
        if contains_ace and t <= 11:
            t += 10
        return t
        
    def is_busted(self):
        return self.total > 21

    def __str__(self):
        rep = self.name + ":\t" + super(BJ_Hand, self).__str__()
        if self.total:
            rep += "(" + str(self.total) + ")" 
        return rep 
    
class BJ_Player(BJ_Hand):
    ''' Игрок в Блек-джек '''
    def is_hitting(self):
        response = games.ask_yes_no("\n" + self.name +
        ", будете брать ещё карты")
        return response == "y"
    

    def bust(self):
        print(self.name, "перебрал(а).")
        self.lose()

    def lose(self):
        print(self.name, "проиграл(а)")

    def win(self):
        print(self.name, "выиграл(а)")

    def push(self):
        print(self.name, "сыграл(а) с дилером вничью")

class BJ_Dealer(BJ_Hand):
    """ Дилер в Блек-джек """
    def is_hitting(self):
        return self.total < 17

    def bust(self):
        print(self.name, "перебрал.")

    def flip_first_card(self):
        first_card = self.cards[0]
        first_card.flip()

class BJ_Game:
    """ Игра в Блек-джек """
    def __init__(self, names):
        self.players = []
        for name in names:
            player = BJ_Player(name)
            self.players.append(player)

        self.dealer = BJ_Dealer("Дилер")

        self.deck = BJ_Deck()
        self.deck.populate()
        self.deck.shuffle()
    
    @property
    def still_playing(self):
        sp = []
        for player in self.players:
            if not player.is_busted():
                sp.append(player)
        return sp

    def __additional_cards(self, player):
        while not player.is_busted() and player.is_hitting():
            self.deck.deal([player])
            print(player)
            if player.is_busted():
                player.bust()
    
    def play(self):
        #сдача всем по две карты
        self.deck.deal(self.players + [self.dealer], per_hand = 2)
        self.dealer.flip_first_card()
        for player in self.players:
            print(player)
        print(self.dealer)

        for player in self.players:
            self.__additional_cards(player)
            self.dealer.flip_first_card()
            if not self.still_playing:
                print(self.dealer)
            else:
                print(self.dealer)
                self.__additional_cards(self.dealer)
                if self.dealer.is_busted():
                    for player in self.still_playing:
                        player.win()
                else:
                    for player in self.still_playing:
                        if player.total > self.dealer.total:
                            player.win()
                        elif player.total < self.dealer.total:
                            player.lose()
                        else:
                            player.push()
            for player in self.players:
                 player.clear()
            self.dealer.clear()
            
def main():
    print("\t\tНу присаживайся, фраерок\n")

    names = []
    name = input("Как тебя звать то?: ")
    names.append(name)
    print()

    game =BJ_Game(names)    
    again = None
    while again != "n":
        game.play()
        again = games.ask_yes_no("\n Деньги еще не все просадил?")

main()