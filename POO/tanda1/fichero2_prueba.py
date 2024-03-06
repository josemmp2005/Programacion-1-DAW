"""
Implementa una clase Point con sus atributos x e y. La clase debe contener: su constructor, los getters y setters
(propiedades), un invert_coordinates() que invierta las coordenadas x e y del punto. Además la clase debe tener
un __str__() para poder imprimir los puntos en formato “(x,y)”. Implementa un test donde crees un punto, lo imprimas
utilizando de manera implícita el método __str__(), imprimas su coordenada x, asignes 0 a su coordenada x, y vuelvas a
imprimir el punto.
Fecha --> 13/01/2024
Author --> José María Mayén Pérez
"""

from fichero2 import Point

p = Point(3,5)
print(f"La coordenada x de {p} es {p.x}")

p.invert_coordinates()
print(f"Punto Invertido --> {p}")

p.x = 0
print(f"Punto modificado --> {p}")


