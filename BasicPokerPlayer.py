from BasicCard import *
from typing import List
import numpy as np


class Hand:

    def __init__(self, player_id: int) -> None:
        self._player_id = player_id
        self._cards = []

    def get_cards(self) -> List[Card]:
        return self._cards

    def set_cards(self, cards: List[Card]) -> None:
        self._cards = cards

    def get_player_id(self) -> int:
        return self._player_id


class Player:

    def __init__(self, player_id: int, player_position: int = 0) -> None:
        self._id = player_id
        self._hand = Hand(player_id)
        self._position = player_position

    def set_hand(self, cards: List[Card]) -> None:
        self._hand.set_cards(cards)

    def get_hand(self) -> Hand:
        return self._hand
