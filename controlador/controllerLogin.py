from modelo.servicios.login import Login

class ControllerLogin:
    def __init__(self, loginServicio: Login):
        self.loginServicio = loginServicio
    
    def login(self, nombre, contrasena):
        return self.loginServicio.accesoSistema(nombre, contrasena)