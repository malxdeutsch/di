# What is a class?
    # It is a new type of object, allowing new instances of that type to be made with methods.
# What is an instance?
    # One object of a class.
# What is encapsulation?
    # The packing of data and functions that work on that data within a single object.
# What is abstraction?
    # Used to hide the internal functionality of the function from the users.
# What is inheritance?
    # Allows to define a class that inherits all the methods and properties from another class.
# What is multiple inheritance?
    # A class can be derived from more than one base class.
# What is polymorphism?
    # The same function name (but different signatures) being used for different types.
# What is method resolution order or MRO?
    # Defines the class search path used by Python to search for the right method to use in classes having multi-inheritance.
import random

suits= ["Hearts", "Diamonds", "Clubs", "Spades"]
values = ["A",2,3,4,5,6,7,8,9,10,"J","Q","K"]

class Card:
    def __init__(self, suits, values):
        self.suit = suits
        self.value = values

    def __repr__(self):
        return f"{self.suit} and {self.value}"


class Deck:
    def __init__(self):
        self.deck = []
    def shuffle_deck(self):
        for suit in suits:
            for value in values:
                self.deck.append(Card(suit, value))
        if len(self.deck) == 52:
            random.shuffle(self.deck)
            return self.deck
        

    def deal(self):
        new_card = random.choice(self.deck)
        self.deck.remove(new_card)
        return new_card



try_one = Deck()
print(try_one.shuffle_deck())
print(try_one.deal())
