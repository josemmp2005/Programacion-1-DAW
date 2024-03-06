"""
9. Nos hemos enterado que la clase datetime.date ha sido comprometida y tenemos que crear una clase nueva para almacenar
fechas locales (Date), en este caso la clase será mutable (los objetos pueden cambiar el día, mes o año). Los objetos de
la clase Fecha son fechas de tiempo y se crean de la forma:

f1 = Date(1, 10, 2020)  # almacena el 1 de Octubre de 2020
f2 = Date(f1)  # almacena una copia de la fecha almacenada en f1

Para simplificar consideraremos que las fechas son todas a partir del 1 de enero del año 1.

Si al constructor se le pasan valores incorrectos lanzaremos la excepción ValueError.

Crea métodos para:

Sumar y restar días a la fecha.
Restar fechas. Devuelve el número de días comprendidos entre ambas.
Comparar la fecha almacenada con otra.
Saber si el año de la fecha almacenada es bisiesto.
Obtener el día de la semana de una fecha concreta.
El método __str__() devuelve una cadena con el formato "<día del mes> de <nombre del mes> de <año>".
"""
from typeguard import typechecked


@typechecked
class Date:

    def __init__(self, day: int, month: int, year: int):
        self.__day = day
        self.__month = month
        self.__year = year

        if not self.__ok_date():
            raise ValueError("Introduce la fecha correctamente")

    @property
    def year(self):
        return self.__year

    @property
    def month(self):
        return self.__month

    @property
    def day(self):
        return self.__day

    def __ok_date(self):
        month_31_days = [1, 3, 5, 7, 8, 10, 12]
        month_30_days = [4, 6, 9, 11]

        if self.__month < 1 or self.__month > 12:
            return False

        if self.__month in month_31_days:
            if self.__day < 1 or self.__day > 31:
                return False
        elif self.__month in month_30_days:
            if self.__day < 1 or self.__day > 30:
                return False
        else:
            # February
            if self.is_leap():
                # Leap year
                if self.__day < 1 or self.__day > 29:
                    return False
            else:
                if self.__day < 1 or self.__day > 28:
                    return False

        return True

    def is_leap(self):
        return self.__year % 4 == 0 and (self.__year % 100 != 0 or self.__year % 400 == 0)

    def tomorrow(self):
        if self.__day == self.month_days():
            if self.__month == 12:
                next_date = Date(1, 1, self.__year + 1)
            else:
                next_date = Date(1, self.__month + 1, self.__year)
        else:
            next_date = Date(self.__day + 1, self.__month, self.__year)

        return next_date

    def yesterday(self):
        days_in_month = self.days_in_month()

        if self.__day == 1:
            if self.__month == 1:
                next_date = Date(days_in_month, self.__month, self.__year - 1)
            else:
                next_date = Date(days_in_month, self.__month - 1, self.__year)
        else:
            next_date = Date(self.__day - 1, self.__month, self.__year)

        return next_date

    def days_in_month(self):
        days_not_leap = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        days_leap = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if self.is_leap():
            days_in_month = days_leap[self.__month - 2]

        else:
            days_in_month = days_not_leap[self.__month - 2]
        return days_in_month

    def month_days(self):
        if self.__month in {1, 3, 5, 7, 8, 10, 12}:
            days_in_month = 31
        elif self.__month in {4, 6, 9, 11}:
            days_in_month = 30
        else:
            # February
            if self.is_leap():
                days_in_month = 29
            else:
                days_in_month = 28

        return days_in_month

    def __add__(self, other: int):
        current_date = self
        for _ in range(other):
            current_date = current_date.tomorrow()

        return current_date

    def __sub__(self, other: int):
        current_date = self
        for _ in range(other):
            current_date = current_date.yesterday()

        return current_date

    def month_str(self):
        months_str = ('Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre',
                      'Noviembre', 'Diciembre')
        return months_str[self.__month - 1]

    def __str__(self):
        return f"{self.__day}-{self.month_str()}-{self.__year}"

    def __eq__(self, other):
        return (self.__day, self.__month, self.__year) == (other.__day, other.__month, other.__year)

    def __le__(self, other):
        return (self.__day, self.__month, self.__year) <= (other.__day, other.__month, other.__year)

    def __gt__(self, other):
        return (self.__day, self.__month, self.__year) > (other.__day, other.__month, other.__year)

    def day_of_week(self):
        d = ((self.__year - 1) % 7 + ((self.__year - 1) // 4 + 3 * ((self.__year - 1) // 100 + 1) // 4)
             % 7 + self.__month + (self.__day % 7)) % 7

        days_in_week = ["Sábado", "Domingo", "Lunes", "Martes", "Miércoles", "Jueves", "Viernes"]
        return days_in_week[d]

