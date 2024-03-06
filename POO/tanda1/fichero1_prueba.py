"""
Crea una clase "Dado" que simule el funcionamiento de un dado con caras del 1 al 6 que tienen la misma probabilidad de
salir y un programa de prueba.
Fecha --> 13/01/2024
Author --> José María Mayén Pérez
"""
from fichero1 import Dado

dice = Dado()

for _ in range(10):
    result = dice.lanzar_dado()
    print(f"Resultado del dado--> {result}")
