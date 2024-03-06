"""
Crea una clase "Fraction" inmutable (no hay setters, solo getters para numerador y denominador) de forma que podamos
hacer las siguientes operaciones:

Construir un objeto Fracción pasándole al constructor el numerador y el denominador. La fracción se construye
simplificada, no se puede dividir por cero.
Obtener resultado de la fracción (número real).
Multiplicar la fracción por un número (el método devuelve otra fracción, simplificada).
Multiplicar, dividir, sumar y restar fracciones (los métodos devuelven otra fracción, simplificada).
Comparar fracciones entre sí o con enteros usando los operadores relacionales.
"""
import math


class Fraction:
    def __init__(self, numerator, denominator):
        if denominator == 0:
            raise ValueError("No se puede dividir por 0")
        gcd = math.gcd(numerator, denominator)  # simplificar fracción usando mcd

        self.__numerator = numerator // gcd
        self.__denominator = denominator // gcd

    @property
    def numerator(self):
        return self.__numerator

    @property
    def denominator(self):
        return self.__denominator

    def __str__(self):
        return f"{self.__numerator} / {self.__denominator}"

    def multiplicate(self, number):
        self.__numerator *= number
        return f"{self.__numerator} / {self.__denominator}"

    def result(self):
        return self.__numerator / self.__denominator

    def __lt__(self, other):
        return self.result() < other.result()

    def __le__(self, other):
        return self.result() > other.result()

    def __eq__(self, other):
        return self.result() == other.result()

    def __add__(self, other):
        new_numerator = (self.__numerator * other.denominator) + (other.numerator * self.__denominator)
        new_denominator = self.__denominator * other.denominator
        return Fraction(new_numerator, new_denominator)

    def __sub__(self, other):
        new_numerator = (self.__numerator * other.denominator) - (other.numerator * self.__denominator)
        new_denominator = self.__denominator * other.denominator
        return Fraction(new_numerator, new_denominator)

    def __mul__(self, other):
        new_numerator = (self.__numerator * other.numerator)
        new_denominator = (self.__denominator * other.denominator)
        return Fraction(new_numerator, new_denominator)

    def __floordiv__(self, other):
        new_numerator = (self.__numerator // other.denominator)
        new_denominator = (self.__denominator // other.numerator)
        return Fraction(new_numerator, new_denominator)

