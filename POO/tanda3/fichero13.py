"""
13. Implementa la clase BankAccount. Cada cuenta corriente tiene un número de cuenta de 10 dígitos. El número de cuenta
se genera de forma aleatoria cuando se crea una cuenta nueva y no puede haber dos objetos con el mismo número de cuenta.
La cuenta se puede crear con un saldo inicial; en caso de no especificar saldo, se pondrá a cero inicialmente.
En una cuenta se pueden hacer ingresos y gastos. También es posible hacer una transferencia entre una cuenta y otra.
No se permite el saldo negativo. En el siguiente capítulo se propone un ejercicio como mejora de este, en el que se pide
llevar un registro de los movimientos realizados.

Programa principal:

cuenta1 = BankAccount()
cuenta2 = BankAccount(1500)
cuenta3 = BankAccount(6000)
print(cuenta1)
print(cuenta2)
print(cuenta3)
cuenta1.deposit(2000)
cuenta2.withdraw(600)
cuenta3.deposit(75)
cuenta1.withdraw(55)
cuenta2. transfer(cuenta3, 100)
print(cuenta1)
print(cuenta2)
print(cuenta3)
Salida

Número de cta: 6942541557 Saldo: 0,00 €
Número de cta: 9319536518 Saldo: 1500,00 €
Número de cta: 7396941518 Saldo: 6000,00 €
Número de cta: 6942541557 Saldo: 1945,00 €
Número de cta: 9319536518 Saldo: 800,00 €
Número de cta: 7396941518 Saldo: 6175,00 €
"""
from random import randint


class BankAccount:
    __account_register = []

    def __init__(self, balance=0):
        self.__number = randint(1, 9999999999)
        self.set_number()
        self.__balance = balance

        while self.__number in self.__account_register:
            self.__number = randint(1, 9999999999)
            self.set_number()

        self.__account_register.append(self.__number)

    @property
    def number(self):
        return self.__number

    @property
    def balance(self):
        return round(self.__number, 2)

    def set_number(self):
        number_str = str(self.__number)
        while len(number_str) != 10:
            number_str = '0' + number_str
        self.__number = number_str

    def deposit(self, money: float):
        if money < 0:
            raise ValueError("NO SE PUEDEN INTRODUCIR NÚMEROS NEGATIVOS")
        self.__balance += money

    def withdraw(self, money: float):
        self.__check_operation(money)
        self.__balance -= money

    def transfer(self, other, money: float):
        self.__check_operation(money)
        self.__balance -= money
        other.__balance += money

    def __check_operation(self, money):
        if money < 0:
            raise ValueError("NO SE PUEDEN INTRODUCIR NÚMEROS NEGATIVOS")
        if money > self.__balance:
            raise ValueError("NO SE PUEDE TENER EL SALDO NEGATIVO")

    def __str__(self):
        return f"Número de cta: {self.__number}, Saldo: {self.__balance} €"


if __name__ == "__main__":
    cuenta1 = BankAccount()
    cuenta2 = BankAccount(1500)
    cuenta3 = BankAccount(6000)
    print(cuenta1)
    print(cuenta2)
    print(cuenta3)
    cuenta1.deposit(2000)
    cuenta2.withdraw(600)
    cuenta3.deposit(75)
    cuenta1.withdraw(55)
    cuenta2.transfer(cuenta3, 100)
    print(cuenta1)
    print(cuenta2)
    print(cuenta3)