"""
14. Crea en Python las siguientes clases:

Card que simule una carta de naipes. Un naipe tiene un palo (de un conjunto de palos) y un valor (de un conjunto de
valores).
CardPlayer que simule un jugador de naipes. Un jugador tiene un conjunto de naipes.
Puede robar una carta de una baraja. Una vez robada el jugador tiene una carta más y la baraja una menos.
Puede deshacerse de una carta.
Puede recibir cartas.
Deck que simula un conjunto de cartas de naipes.
Inicialmente tiene las cartas que le llegan con el constructor.
Puede repartir un conjunto de cartas a un jugador. En la baraja dejan de existir esas cartas.
Le pueden quitar la primera carta (robar).
Puede barajarse.
Baraja Española e Inglesa (SpanishDeck e EnglishDeck) que heredan de Deck.
"""
from fichero14_card import Card
import random


class Deck:

    def __init__(self, card: list[Card]):
        self.__cards = card

    def deal(self, player, number: int):
        if number < 0:
            raise ValueError("DEBES PASAR UN NUMERO POSITIVO")
        if number > len(self.__cards):
            raise ValueError("CARTAS INSUFICIENTES")

        cards_to_deal = []
        for _ in range(number):
            for card in self.__cards:
                cards_to_deal.append(card)  # TODO

        player.receive_cards(cards_to_deal)

    def steal(self):
        if len(self.__cards) == 0:
            raise ValueError("NO QUEDAN MÁS CARTAS EN LA BARAJA")
        return self.__cards.pop(0)

    def mix(self):
        random.shuffle(self.__cards)
