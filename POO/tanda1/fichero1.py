"""
Crea una clase "Dado" que simule el funcionamiento de un dado con caras del 1 al 6 que tienen la misma probabilidad de
salir y un programa de prueba.
Fecha --> 13/01/2024
Author --> José María Mayén Pérez
"""
import random


class Dado:
    def __init__(self):
        self.__FACES = 6

    def lanzar_dado(self):
        return random.randint(1, self.__FACES)
