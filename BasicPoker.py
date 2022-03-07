from BasicCard import *
from BasicPokerPlayer import Player, Hand
from typing import List


NUM_COMMUNITY_CARDS = 5


class HandRank:
    HIGH_CARD = 0
    PAIR = 1
    TWO_PAIR = 2
    THREE_OF_KIND = 3
    STRAIGHT = 4
    FLUSH = 5
    FULL_HOUSE = 6
    FOUR_OF_KIND = 7
    STRAIGHT_FLUSH = 8


class HandEvaluator:
    
    def __init__(self) -> None:
        self._community_cards = []
        self._player_hands = []

    def set_community_cards(self, cards: List[Card]) -> None:
        assert(len(cards) == NUM_COMMUNITY_CARDS)
        self._community_cards = cards

    def set_player_hands(self, hands: List[Hand]) -> None:
        self._player_hands = hands

    def _check_pair(self, hand: Hand) -> bool:
        """
        Change to finding most common integer in a list of integers converted from string values of cards
        """
        # Get Hand cards
        card_1, card_2 = hand.get_cards()
        card_1_val = card_1.get_value()
        card_2_val = card_2.get_value()
        
        # Check if hand is a pair
        if (card_1_val == card_2_val):
            return True

        # Check if hand per card
        for card in self._community_cards:
            current_card_val = card.get_value()
            if (current_card_val == card_1_val or current_card_val == card_2_val):
                return True
        return False

    def _get_highest_hand_rank(self, hand: Hand) -> HandRank:
        # Check Pair
        if (self._check_pair(hand)):
            pass
            ## Check Three of Kind
            ## Check Two Pair
            ### Check Four of Kind
            ### Check Full House

        # Check for Straight
        ## Check for Flush Straigh

        # Check for Flush

        # Return High Card

        pass

    def _compare_hands(hand_1: Hand, hand_2: Hand) -> int:
        """
        Return
        - 0 if equivalent hands
        - 1 if player 1
        - 2 if player 2
        """

        # If Same Rank, check which 5 cards is higher in numbers
        pass

    def evaluate_hands(self) -> int:
        winning_hands = []
        while len(self._player_hands) > 0:
            current_hand = self._player_hands.pop()
            if len(winning_hands == 0):
                winning_hands.append(current_hand)
            else:
                winning_hand = winning_hands[0]
                hand_comparison_value = self._compare_hands(current_hand, winning_hand)
                if (hand_comparison_value == 0):
                    winning_hands.append(current_hand)
                elif (hand_comparison_value == 2):
                    winning_hands = [current_hand]
        return [hand.get_player_id() for hand in winning_hands]


if __name__ == "__main__":
    player_hand_1 = Hand(1)
    player_hand_1.set_cards([Card(CardValue.TWO, CardSuit.CLUB), Card(CardValue.ACE, CardSuit.DIAMOND)])
    print("Player Hand")
    for card in player_hand_1.get_cards():
        print(card, end="")
    print("\n")

    com_card_1 = Card(CardValue.TWO, CardSuit.CLUB)
    com_card_2 = Card(CardValue.KING, CardSuit.CLUB)
    com_card_3 = Card(CardValue.JACK, CardSuit.CLUB)
    com_card_4 = Card(CardValue.TEN, CardSuit.CLUB)
    com_card_5 = Card(CardValue.THREE, CardSuit.CLUB)
    community_cards = [com_card_1, com_card_2, com_card_3, com_card_4, com_card_5]
    print("Community Cards")
    for card in community_cards:
        print(card, end="")
    print("\n")

    evaluator = HandEvaluator()
    evaluator.set_community_cards(community_cards)
    print(evaluator._check_pair(player_hand_1))
