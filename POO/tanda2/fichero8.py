"""
Muestra un menú con las siguientes opciones:

- Introducir (por teclado) una fecha pidiendo por teclado año, mes y día en formato dd/mm/aaaa. Si no se introduce
correctamente se devuelve un mensaje de error. Usa una función booleana para validar la fecha.
- Añadir días a la fecha. Pide un número de días para sumar a la fecha introducida previamente y actualiza su valor.
Si el número es negativo restará los días. Esta opción sólo podrá realizarse si hay una fecha introducida (se ha
ejecutado la opción anterior), si no la hay mostrará un mensaje de error.
- Añadir meses a la fecha. El mismo procedimiento que la opción anterior.
- Añadir años a la fecha. El mismo procedimiento que la opción 2.
Comparar la fecha introducida con otra. Pide una fecha al usuario en formato dd/mm/aaaa (válida, si no lo es da error)
y la comparará con la que tenemos guardada, posteriormente mostrará si esta fecha es anterior, igual o posterior a la
 que tenemos almacenada y el número de días comprendido entre las dos fechas.
Mostrar la fecha en formato largo (ejemplo: "lunes, 1 de febrero de 2021").
Terminar.
"""
import datetime


class Menu:
    def __init__(self, titles, *options):
        self.__title = titles
        self.__options = options

    @property
    def title(self):
        return self.__title

    @property
    def options(self):
        return self.__options

    def print_menu(self):
        print(self.__title)
        for option in self.__options:
            print(option)


if __name__ == "__main__":
    title = "MENU"
    options = ["1. Introducir una fecha en formato dd/mm/aaaa.", "2. Añadir días a la fecha.", "3. Añadir meses a "
               "la fecha", "4. Añadir años a la fecha", "5. Comparar fechas", "6. Mostrar fecha en formato largo",
               "7. Terminar"]

    menu = Menu(title, *options)
    menu.print_menu()
