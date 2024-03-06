"""
Implementar otra clase Dado. Por defecto el dado tendrá 6 caras. Tendremos tres formar de construir un dado (uno al que
no se le pasa nada e inicializa el dado al azar, otro al que sólo se le pasa que número tiene el dado en la cara
superior y otro con el número del dado en la cara superior y el número de caras del dado). Implementa los getters,
el método roll() que tirará el dado al azar y el __str__(). Implementa un tester que tenga un vector de 4 dados y los
lance una serie de veces.
Fecha --> 18/01/2024
Author --> José María Mayén Pérez
"""
from fichero4 import Dice

dices = [Dice(), Dice(4), Dice(7, 8)]


throw = int(input("¿Cuantas veces quieres lanzar los dados?: "))
for i in range(throw):
    print(f"Lanzamiento {i + 1}:")
    for dice in dices:
        dice.roll()
        print(dice)
    print()