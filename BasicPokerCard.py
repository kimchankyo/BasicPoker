from typing import List
import random


class CardValue:
    ACE = "A"
    TWO = "2"
    THREE = "3"
    FOUR = "4"
    FIVE = "5"
    SIX = "6"
    SEVEN = "7"
    EIGHT = "8"
    NINE = "9"
    TEN = "10"
    JACK = "J"
    QUEEN = "Q"
    KING = "K"

    """ Customizable order depen"""
    STRENGTH_ORDER = [TWO, THREE, FOUR, FIVE, SIX, SEVEN, EIGHT, NINE, TEN, JACK, QUEEN, KING, ACE]


class CardSuit:
    SPADE = "\u2664"
    CLUB = "\u2667"
    HEART = "\u2665"
    DIAMOND = "\u2666"


class Card:
    def __init__(self, card_value: CardValue, card_suit: CardSuit) -> None:
        self.value = card_value
        self.suit = card_suit

    def __str__(self) -> str:
        return self.suit + self.value
    
    def get_value(self) -> CardValue:
        return self.value

    def get_suit(self) -> CardSuit:
        return self.suit
        
        
class Deck:
    def __init__(self) -> None:
        self.deck = [Card(getattr(CardValue, card_value), getattr(CardSuit, card_suit)) 
                     for card_value in dir(CardValue) if card_value.find("_") == -1
                     for card_suit in dir(CardSuit) if card_suit.find("_") == -1]
        self.length = len(self.deck)
        random.shuffle(self.deck)
    
    def __str__(self) -> str:
        string = "Number of Cards In Deck: " + str(self.length) + "\nOrder:\n"
        for i in range(self.length):
            string += str(self.deck[i]) + "\n"
        return string
    
    def draw_card(self) -> Card:
        if self.length > 0:
            self.length -= 1
            return self.deck.pop()
    
    def draw_hand(self, num_cards: int) -> List[Card]:
        if self.length >= num_cards:
            hand = []
            for i in range(num_cards):
                hand.append(self.deck.pop())
            return hand


if __name__ == "__main__":
    deck = Deck()
    print(deck)
    

    
