import random
from typing import List
from typeguard import typechecked
from card import Card


@typechecked
class Deck:

    def __init__(self, cards: List[Card]):
        self.__cards = list(cards)

    @property
    def size(self):
        return len(self.__cards)

    def deal(self, player, number: int):
        if number < 0:
            raise ValueError("El número de cartas a repartir tiene que ser positivo")
        if number > len(self.__cards):
            raise ValueError("No hay cartas suficientes para repartir")

        cards_to_deal = self.__cards[:number]
        player.receives(cards_to_deal)
        self.__cards = self.__cards[number:]

    def draw(self):
        if self.size == 0:
            raise ValueError("No quedan cartas en la baraja")
        return self.__cards.pop(0)

    def shuffle(self):
        random.shuffle(self.__cards)

    def __repr__(self):
        return repr(self.__cards)