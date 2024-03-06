"""
Implementa la clase Rectangulo (determinado por dos objetos Point) que además de su constructor, tendrá dos métodos para
calcular su área y su perímetro que tienes que transformar en propiedades. Implementa también un test que cree dos
puntos y un rectángulo a partir de estos dos puntos y que muestre el área y perímetro de dicho rectángulo.
Fecha --> 18/01/2024
Author --> José María Mayén Pérez

"""
from fichero2 import Point
from fichero3 import Rectangulo

p1 = Point(2, 5)
p2 = Point(5, 10)

rectangle = Rectangulo(p1, p2)

print(rectangle)
print(f"Area = {rectangle.area}")
print(f"Perimetro = {rectangle.perimetro()}")
