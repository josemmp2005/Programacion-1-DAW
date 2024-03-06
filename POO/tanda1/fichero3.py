"""
Implementa la clase Rectangulo (determinado por dos objetos Point) que además de su constructor, tendrá dos métodos para
calcular su área y su perímetro que tienes que transformar en propiedades. Implementa también un test que cree dos
puntos y un rectángulo a partir de estos dos puntos y que muestre el área y perímetro de dicho rectángulo.
Fecha --> 18/01/2024
Author --> José María Mayén Pérez

"""
from fichero2 import Point

class Rectangulo:

    def __init__(self, p1: Point, p2: Point):
        self.p1 = p1
        self.p2 = p2

    @property
    def p1(self):
        return self.__p1

    @p1.setter
    def p1(self, value):
        self.__p1 = value

    @property
    def p2(self):
        return self.__p2

    @p2.setter
    def p2(self, value):
        self.__p2 = value

    @property
    def area(self):
        area = abs((self.p1.x - self.p2.x) * (self.p1.y - self.p2.y))
        return area

    def perimetro(self):
        perimetre = 2 * (abs(self.p1.x - self.p2.x) - (self.p1.y - self.p2.y))
        return perimetre

    def __str__(self):
        return f"({self.p1.x}, {self.p1.y})"
