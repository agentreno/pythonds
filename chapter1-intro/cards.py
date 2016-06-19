from enum import Enum

class Rank(Enum):
    ace = 1
    two = 2
    three = 3
    four = 4
    five = 5
    six = 6
    seven = 7
    eight = 8
    nine = 9
    ten = 10
    jack = 11
    queen = 12
    king = 13

class Suit(Enum):
    spades = 1
    clubs = 2
    hearts = 3
    diamonds = 4

class Card:

    def __init__(self, rank, suit):
        if isinstance(rank, Rank) and isinstance(suit, Suit):
            self.rank = rank
            self.suit = suit
        else:
            raise TypeError("Rank and suit must be defined with the Rank and Suit enum types")

    def __repr__(self):
        return str(self.rank) + " " + str(self.suit)

    def __str__(self):
        return "The " + self.rank.name.capitalize() + " of " + \
            self.suit.name.capitalize()

class Deck:

    def __init__(self):
        self.cards = [Card(rank, suit) for suit in Suit for rank in Rank] 

    def __repr__(self):
        return str(self.cards)

    def __str__(self):
        return str(self.cards)
