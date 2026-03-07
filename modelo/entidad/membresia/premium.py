from .membresia import Membresia

class Premium(Membresia):
    @property
    def limite_prestamos(self):
        return 10