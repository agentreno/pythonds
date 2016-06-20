import random
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

    def pickRandomCard(self):
        return self.cards.pop(random.randint(0, len(self.cards) - 1))

if __name__ == "__main__":
    print("==Pontoon==")
    deck = Deck()
    chooseAgain = True
    total = 0

    while chooseAgain:
        choice = input("Your score is " + str(total) + \
            ". Do you want to stick or twist? ")
        if choice == "stick" or choice == "s":
            chooseAgain = False
        elif choice == "twist" or choice == "t":
            card = deck.pickRandomCard()
            print("You drew: " + str(card))
            if card.rank.value == 1:
                aceChooseAgain = True
                while aceChooseAgain:
                    acechoice = input("An ace can count for 1 or 11 points." + \
                        " Which would you like? ")
                    if acechoice == "one" or acechoice == "1":
                        total += 1
                        aceChooseAgain = False
                    elif acechoice == "eleven" or acechoice == "11":
                        total += 11
                        aceChooseAgain = False
                    else:
                        print("I didn't understand your choice.")

            elif card.rank.value > 10:
                total += 10
            else:
                total += card.rank.value

            if total >= 21:
                chooseAgain = False
        else:
            print("I didn't recognise your choice.")

    if total > 21:
        print("You went bust with a score of " + str(total))
    elif total == 21:
        print("You got a perfect score of 21")
    else:
        print("You stuck at " + str(total))

