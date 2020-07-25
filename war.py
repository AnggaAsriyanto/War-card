from random import shuffle

class Card:

    suits = ['spades', 'hearts', 'diamonds', 'clubs']

    values = ['2', '3', '4', '5', '6', '7', '9', '10', 'Jack', 'Queen', 'King', 'Ace']

    def __init__(self, v, s):
        self.value = v
        self.suit = s

    def __lt__(self, other):
        if self.value < other.value:
            return True
        if self.value == other.value:
            if self.suit < other.suit:
                return True
            else:
                return False
        else:
            return False
    def __gt__(self, other):
        if self.value > other.value:
            return True
        if self.value == other.value:
            if self.suit > other.suit:
                return True
            else:
                return False
        else:
            return False

    def __repr__(self):
        v = self.values[self.value] + " of " + self.suits[self.suit]
        return v

class Deck:
    def __init__(self):
        self.cards = []
        for i in range(0, 13):
            for j in range(4):
                self.cards.append(Card(i, j))
        shuffle(self.cards)

    def rm_card(self):
        if len(self.cards) == 0:
            return
        return self.cards.pop()

class Player:
    def __init__(self, name):
        self.name = name
        self.wins = 0
        self.card = None

class Game:
    def __init__(self):
        name1 = input('p1 name: ')
        name2 = input('p2 name: ')
        self.deck = Deck()
        self.p1 = Player(name1)
        self.p2 = Player(name2)
        if self.p1.name == self.p2.name:
            print("Your name must to be different from p1")


    def wins(self, winner):
        w = 'Winner this round is {}'
        w = w.format(winner)
        print(w)

    def draw(self, p1n, p1c, p2n, p2c):
        d = '{} drew {} and {} drew {}'
        d = d.format(p1n, p1c, p2n, p2c)
        print(d)

    def play_game(self):
        self.cards = self.deck.cards
        while len(self.cards) >= 2:
            m = "enter q to quit.Any key to play: "
            response = input(m)
            if response == "q":
                break
            p1c = self.deck.rm_card()
            p2c = self.deck.rm_card()
            p1n = self.p1.name
            p2n = self.p2.name
            self.draw(p1n, p1c, p2n, p2c)
            if p1c > p2c:
                self.p1.wins += 1
                self.wins(self.p1.name)
                print('\n')
            else:
                self.p2.wins += 1
                self.wins(self.p2.name)
                print('\n')
        win = self.winner(self.p1, self.p2)
        print("War is over. {} wins".format(win))

    def winner(self, p1, p2):
        if p1.wins > p2.wins:
            return self.p1.name
        else:
            return self.p2.name

game = Game()
game.play_game()
