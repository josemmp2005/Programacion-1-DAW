from fichero10_vehicule_class import Vehicle


class Bicicleta(Vehicle):

    def __init__(self):
        super().__init__()

    def viaje(self, km: int):
        super().travel(km)
        return (" -------- __@      __@       __@       __@      __~@ \n"
                " -----  _`\<,_   _`\<,_    _`\<,_    _`\<,_   _`\<,_ \n"
                " ---- (*)/ (*)  (*)/ (*)  (*)/ (*)  (*)/ (*)  (*)/ (*) \n"
                " ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~  \n")

    @staticmethod
    def caballito():
        return ("                o       o       o      o\n "
                "       _o      /\_     /\_     /\_    /\_\n "
                "     _< \_     _>(_)   _>(_)   _>(_)  _>(_) \n"
                "     (_)>(_) (_)     (_)     (_)    (_)")
