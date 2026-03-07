from modelos import usuario
from modelos.membresia import basica, premium

class AsignarMembresia:
    def asignarBasica(self, usuario: usuario.Usuario):
        membresia = basica.Basica()
        usuario.membresia = membresia

    def asignarPremium(self, usuario: usuario.Usuario, membresia: premium.Premium = "Premium"):
        usuario.membresia = membresia