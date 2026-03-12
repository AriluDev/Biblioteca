from controlador.controllerLogin import ControllerLogin

class InicioSesionVista:

    def mostrar(self, controller: ControllerLogin):
        print("BIBLIOTECA \n")
        nombre = input("Nombre del Usuario: ")
        contrasena = input("Contraseña: ")
        usuario = controller.login(nombre, contrasena)
        return usuario