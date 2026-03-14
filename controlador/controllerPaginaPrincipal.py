from modelo.servicios.servicioPaginaPrincipal import ServicioPaginaPrincipal

class ControllerPaginaPrincipal:
    def __init__(self, servicio: ServicioPaginaPrincipal):
        self.servicio = servicio
