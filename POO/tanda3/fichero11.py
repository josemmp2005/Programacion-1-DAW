"""
11. Implementa la clase Terminal. Un terminal tiene asociado un número de teléfono. Los terminales se pueden llamar unos
a otros y el tiempo de conversación corre para ambos. A continuación se proporciona el contenido del programa principal
que usa esta clase y el resultado que debe aparecer por pantalla. Los números de teléfono tienen que validarse como
tales al crear el objeto (solo dígitos, empiezan por 9, 6 ó 7, su longitud es de nueve dígitos) y no puede haber dos
terminales con el mismo número.

Programa principal:

t1 = Terminal("678112233")
t2 = Terminal("644744469")
t3 = Terminal("622328909")
t4 = Terminal("664739818")
print(t1)
print(t2)
t1.call(t2, 320)
t1.call(t3, 200)
print(t1)
print(t2)
print(t3)
print(t4)
Salida:

No 678 11 22 33 - 0s de conversación
No 644 74 44 69 - 0s de conversación
No 678 11 22 33 - 520s de conversación
No 644 74 44 69 - 320s de conversación
No 622 32 89 09 - 200s de conversación
No 664 73 98 18 - 0s de conversación

DATE: 26-02-2024
AUTHOR: JOSÉ MARÍA MAYÉN PÉREZ
"""


class Terminal:
    __register = []
    NUMBER_LENGTH = 9

    def __init__(self, number: str):
        self.__number = number
        self.__time_talking = 0

        if not self.ok_number():
            raise ValueError("INTRODUZCA EL NUMERO CORRECTAMENTE")

        self.__register.append(self.__number)

    def ok_number(self):

        if int(self.__number) < 0:
            raise ValueError("UN NUMERO DE TELÉFONO NO PUEDE SER NEGATIVO")
        if len(str(self.__number)) != self.NUMBER_LENGTH:
            raise ValueError("UN NUMERO DEBE TENER 9 DÍGITOS")
        if int(str(self.__number)[0]) not in (9, 6, 7):  # primer número
            raise ValueError("EL NUMERO DEBE EMPEZAR POR 9, 6 o 7")
        if self.__number in self.__register:
            raise ValueError("NO PUEDE HABER DOS TERMINALES CON EL MISMO NUMERO")
        else:
            return True

    def call(self, other: 'Terminal', time):
        if time < 0:
            raise ValueError("EL TIEMPO DEBE SER MAYOR A 0")
        if self.__number == other:
            raise ValueError("NO PUEDES LLAMAR AL MISMO NUMERO")
        self.__time_talking += time
        other.__time_talking += time

    def __str__(self):
        return (f"No {str(self.__number)[:3]} {str(self.__number)[3:6]} {str(self.__number)[-3:]} - "
                f"{self.__time_talking}s de conversación")


if __name__ == '__main__':
    t1 = Terminal("678112233")
    t2 = Terminal("644744469")
    t3 = Terminal("622328909")
    t4 = Terminal("664739818")
    print(t1)
    print(t2)
    t1.call(t2, 320)
    t1.call(t3, 200)
    print(t1)
    print(t2)
    print(t3)
    print(t4)