from fichero10_vehicule_class import Vehicle


class Car(Vehicle):
    LITER_PER_KM = 0.1

    def __init__(self):
        super().__init__()
        self.__liters_left_in_tank = 0

    @property
    def liters_left_in_tank(self):
        return self.__liters_left_in_tank

    def fill_tank(self):
        FULL_TANK_CAPACITY = 50  # TODO hacer variable de clase
        self.__liters_left_in_tank = FULL_TANK_CAPACITY
        return print("   .------. \n"
                     "   |==  ==|-. \n"
                     "   |~~ ~~~|`\|  \n"
                     "   | GAS  | ||  \n"
                     "   |      |//  \n"
                     "   |      |/ \n"
                     "   |      | \n"
                     " __|______|___ \n"
                     "[____________]")

    def travel(self, km: int):  # TODO CAMBIAR INT A FLOAT
        if self.__liters_left_in_tank > km * self.LITER_PER_KM:
            super().travel(km)
            self.__liters_left_in_tank -= km * self.LITER_PER_KM
            return print("                        ..-------++._ \n"
                         "                       _.-'/ |      _||  \"--._ \n "
                         "                __.--'`._/_\j_____/_||___\    `---- \n"
                         "           _.--'_____    |          \     _____    |    -  _  __ ___ __ ___\n"
                         "        _j    /,---.\   |        =o |   /,---.\   |_    _ - _ - _  -__  _ _ \n"
                         "       [__]==// .-. \\==`===========/==// .-. \\=[__] - _ - _   - - - -_  - -\n"
                         "         `-._|\ `-' /|___\_________/___|\ `-' /|_.'  _ - -  _  - -__  -    )\n"
                         "               `---'                     `---'   -")
        else:
            raise ValueError("Combustible Insuficiente")    # TODO QUITAR EL Y PONER CLAUSULA DE GUARDA

    @staticmethod
    def quemar_rueda():
        return ("                            ..-------++._ \n"
                "                       _.-'/ |      _||  \"--._ \n "
                "                __.--'`._/_\j_____/_||___\    `---- \n"
                "           _.--'_____    |          \     _____    |       -  _ ___ \n"
                "        _j    /,---.\   |        =o |   /,---.\   |_    -4 ((  -      )  \n"
                "       [__]==// .-. \\==`===========/==// .-. \\=[__] - ( - VROOOOMv!!! )\n"
                "         `-._|\ `-' /|___\_________/___|\ `-' /|_.'  _ - (-     -    )\n"
                "               `---'                     `---'   -")
