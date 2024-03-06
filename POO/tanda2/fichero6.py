"""
6. Crea una clase para almacenar duraciones de tiempo (Duration). Los objetos de esta clase son intervalos de tiempo y
se crean de la forma:

t1 = Duration(1, 20, 30)  # almacenará 1 hora, 20 minutos y 30 segundos.

t2 = Duration(2, 75, -10)  # almacenará 3 horas, 14 minutos y 50 segundos.

t3 = Duration(t2)  # almacenará las horas, minutos y segundos del objeto t2

Crea los getters y setters mediante propiedades y métodos para:

Sumar y restar objetos de la clase sobrecargando operadores (el resultado es otro objeto).
Sumar y restar segundos, minutos o horas (se cambia el objeto actual).
Devolver una cadena con el tiempo almacenado, de forma que si lo que hay es (10 35 5) la cadena sea 10h 35m 5s.
"""


class Duration:
    def __init__(self, hours=0, minutes=0, seconds=0):
        self.__hours = hours
        self.__minutes = minutes
        self.__seconds = seconds

        while self.__seconds >= 60:
            self.__minutes += 1
            self.__seconds -= 60

        while self.__minutes >= 60:
            self.__hours += 1
            self.__minutes -= 60

        while self.__seconds < 0:
            self.__minutes -= 1
            self.__seconds += 60

        while self.__minutes < 0:
            self.__hours -= 1
            self.__minutes += 60

    def __str__(self):
        return f"{self.__hours}h {self.__minutes}m {self.__seconds}s"

    @property
    def hours(self):
        return self.__hours

    @property
    def minutes(self):
        return self.__minutes

    @property
    def seconds(self):
        return self.__seconds

    @hours.setter
    def hours(self, value):
        self.__hours = value

    @minutes.setter
    def minutes(self, value):
        self.__minutes = value

    @seconds.setter
    def seconds(self, value):
        self.__seconds = value

    def add_hours(self, a):
        self.__hours += a

    def add_minutes(self, a):
        self.__minutes += a

    def add_seconds(self, a):
        self.__seconds += a

    def sub_hours(self, a):
        self.__hours -= a

    def sub_minutes(self, a):
        self.__minutes -= a

    def sub_seconds(self, a):
        self.__seconds -= a

    def __add__(self, other):
        return Duration(self.__hours + other.__hours, self.__minutes + other.__minutes,
                        self.__seconds + other.__seconds)

    def __sub__(self, other):
        return Duration(self.__hours - other.__hours, self.__minutes - other.__minutes,
                        self.__seconds - other.__seconds)
