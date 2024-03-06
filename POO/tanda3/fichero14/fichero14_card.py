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


class Card:

    def __init__(self, suit: str, value: str):
        self.__suit = suit
        self.__value = value

    def suit(self):
        return self.__suit

    def value(self):
        return self.__value

    def __str__(self):
        return f"{self.suit}, {self.value}"
