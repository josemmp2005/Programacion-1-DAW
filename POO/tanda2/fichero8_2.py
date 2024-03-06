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
import locale
from datetime import datetime, timedelta
from fichero8 import Menu
from dateutil.relativedelta import relativedelta

locale.setlocale(locale.LC_ALL, 'es_ES')

title = "MENU"
options = ["1. Introducir una fecha en formato dd/mm/aaaa.", "2. Añadir días a la fecha.", "3. Añadir meses a "
           "la fecha", "4. Añadir años a la fecha", "5. Comparar fechas", "6. Mostrar fecha en formato largo",
           "7. Terminar"]

menu = Menu(title, *options)


def main():
    date = None
    while True:
        menu.print_menu()
        choice = int(input())
        if choice == 1:
            date = input_date()
        elif choice == 2:
            print(add_days(date))
        elif choice == 3:
            print(add_month(date))
        elif choice == 4:
            add_years(date)
        elif choice == 5:
            print(compare_dates(date))
        elif choice == 6:
            print(str_date(date))
        elif choice == 7:
            break
        else:
            print("INTRODUCE BIEN LAS OPCIONES")


def input_date():
    year = int(input("Introduce años: "))
    month = int(input("Introduce meses: "))
    day = int(input("Introduce dias: "))
    date = datetime(year, month, day).date()
    return date


def add_days(date):
    days_add = int(input("Introduce los dias que quieras añadir: "))
    date += timedelta(days=days_add)
    return date


def add_month(date):
    months_add = int(input("Introduce los meses que quieras añadir: "))
    date += relativedelta(months=months_add)
    return date


def add_years(date):
    years_add = int(input("Introduce los años que quieras añadir: "))
    date += relativedelta(years=years_add)
    return date


def compare_dates(date):
    if date is None:
        return f"Introduce primero una fecha"

    print("Introduce otra fecha para comparar")
    date2 = input_date()

    if date < date2:
        return f"{date} es anterior que {date2}"
    if date > date2:
        return f"{date} es posterior que {date2}"
    else:
        return f"Son la misma fecha"


def str_date(date):
    if date:
        string_date = date.strftime("%A, %d de %B de %Y")
        return string_date

    else:
        print("Error: Primero debes introducir una fecha.")


if __name__ == "__main__":
    main()
