"""
Implementar otra clase Dado. Por defecto el dado tendrá 6 caras. Tendremos tres formar de construir un dado (uno al que
no se le pasa nada e inicializa el dado al azar, otro al que sólo se le pasa que número tiene el dado en la cara
superior y otro con el número del dado en la cara superior y el número de caras del dado). Implementa los getters,
el método roll() que tirará el dado al azar y el __str__(). Implementa un tester que tenga un vector de 4 dados y los
lance una serie de veces.
Date --> 22/01/2024
Author --> José María Mayén Pérez
"""

import random

DEFAULT_FACES = 6


class Dice:
    def __init__(self, top_face=random.randint(1, DEFAULT_FACES), faces=DEFAULT_FACES):
        if faces <= 0:
            raise ValueError("El número de caras no puede ser menor que 0")
        self.__faces = faces

        if top_face <= 0 or top_face > faces:
            raise ValueError("El valor del dado no puede ser mayor que el número de caras que hay")
        self.__top_face = top_face

    @property
    def faces(self):
        return self.__faces

    @property
    def top_face(self):
        return self.__top_face

    def roll(self):
        self.__top_face = random.randint(1, self.__faces)

    def __str__(self):
        return f"Dado con {self.__faces} caras --> Resultado = {self.__top_face}"
