from .membresia import Membresia

class Basica(Membresia):
    
    @property
    def limite_prestamos(self):
        return 5