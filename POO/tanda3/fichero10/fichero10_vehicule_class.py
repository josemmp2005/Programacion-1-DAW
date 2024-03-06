from abc import ABC
from typeguard import typechecked


class Vehicle(ABC):
    vehicles_created = 0
    total_kilometers = 0

    def __init__(self):
        self.__kilometers_traveled = 0
        Vehicle.vehicles_created += 1

    def kilometres_traveled(self):
        return self.__kilometers_traveled

    def travel(self, km: int):
        if km < 0:
            raise ValueError("Los kilómetros no pueden ser negativos")
        self.__kilometers_traveled += km
        Vehicle.total_kilometers += km
