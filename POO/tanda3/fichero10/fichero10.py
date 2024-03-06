"""
10. Crea la clase abstracta Vehicle, así como las clases Bike y Car como subclases de la primera. Para la clase Vehicle,
crea los atributos de clase vehicles_created y total_kilometers, así como el atributo de instancia kilometers_traveled.

En la clase Vehicle crea un método para viajar (travel) que incremente los kilómetros recorridos.

En la clase Bike haz un método para hacer el caballito.

En la clase Car:

Tendremos una variable de instancia con los litros de combustible que quedan en el deposito, inicialmente cero.
Tendremos un método para quemar rueda y otro para llenar el depósito.
Cuando el coche viaje disminuirá el número de litros en el depósito en relación a los kilómetros viajados. Si no hay
combustible suficiente, el coche recorrerá únicamente los kilómetros que pueda. Para simplificar, cada kilómetro
recorrido consumirá 0,1 litros de combustible, en un depósito caben 50 litros y quemar rueda consume 1 litro de
combustible. Prueba las clases creadas mediante un programa con un menú (usando la clase de la tanda anterior) como
 el que se muestra a continuación:

VEHÍCULOS
=========
1. Anda con la bicicleta.
2. Haz el caballito con la bicicleta.
3. Anda con el coche.
4. Quema rueda con el coche.
5. Llena el depósito del coche.
6. Ver kilometraje de la bicicleta.
7. Ver kilometraje del coche.
8. Ver el combustible que queda en el depósito del coche.
9. Ver kilometraje total.
10. Salir.

Author: José María Mayén Pérez
Date: 16-02-2024
"""

from fichero10_vehicule_class import Vehicle
from POO.tanda2.fichero8 import Menu
from fichero10_coche import Car
from fichero10_bicicleta import Bicicleta


# noinspection PyArgumentList
def main():
    bicicleta = Bicicleta()
    coche = Car()

    while True:
        menu.print_menu()
        choice = int(input("Seleccione una opción: "))

        if choice == 1:
            km = int(input("Cuantos KM anda la bicicleta?: "))
            print(bicicleta.viaje(km))

        elif choice == 2:
            print(Bicicleta.caballito())

        elif choice == 3:
            km = int(input("Cuantos KM viaja el coche?: "))
            print(coche.travel(km))

        elif choice == 4:
            print(Car.quemar_rueda())

        elif choice == 5:
            coche.fill_tank()

        elif choice == 6:
            print("Kilometraje de la bicicleta:", bicicleta.kilometres_traveled())

        elif choice == 7:
            print("Kilometraje del coche:", coche.kilometres_traveled())

        elif choice == 8:
            print("Combustible en el depósito del coche:", coche.liters_left_in_tank)

        elif choice == 9:
            print("Kilometraje total:", Vehicle.total_kilometers)

        elif choice == 10:
            print("Saliendo del programa...")
            break

        else:
            print("OPCIÓN INCORRECTA")


if __name__ == "__main__":
    title = "VEHICULES"
    options = ["=========", "1. Anda con la bicicleta", "2. Haz el caballito con la bicicleta.", "3. Anda con el coche.",
               "4. Quema rueda con el coche.", "5. Llena el depósito del coche.", "6. Ver kilometraje de la bicicleta.",
               "7. Ver kilometraje del coche.", "8. Ver el combustible que queda en el depósito del coche.",
               "9. Ver kilometraje total.", "10. Salir."]

    menu = Menu(title, *options)
    main()
