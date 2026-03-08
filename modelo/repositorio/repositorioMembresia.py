from modelo.entidad.membresia import Membresia

class RepositorioMembresia():
    def __init__(self):
        self.__membresias = []
    
    def agregarMembresias(self, *membresias: Membresia):
        coincidencias = []

        for membresia in membresias:
            if any(membresia.nombre == existente.nombre for existente in self.__membresias):
                coincidencias.append(membresia)
            else:
                self.__membresias.append(membresia)

        if coincidencias:
            print(f"Las siguientes membresias no ha sido agregadas por que ya existen {coincidencias}")

    def buscarPorNombre(self, nombre):
        for membresia in self.__membresias:
            if nombre == membresia.nombre:
                return membresia
