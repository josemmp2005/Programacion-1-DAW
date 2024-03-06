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
from fichero14_deck import Deck
from fichero14_card import Card


class CardPlayer:

    def __init__(self, name: str):
        self.__hand = []
        self.__name = name

    @property
    def cards(self):
        return self.__hand.copy()

    @property
    def name(self):
        return self.__name

    def discard_card(self, card: Card):
        if card in self.__hand:
            self.__hand.remove(card)
            return card
        else:
            raise ValueError(f"{card}, NO ESTA EN LA MANO")

    def steal(self):
        pass

    def receive(self, cards: list):
        self.__hand.extend(cards)

