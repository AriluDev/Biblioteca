from vista import limpiar_pantalla
from modelo.entidad.usuario import Usuario
from modelo.repositorio.repositorioLibro import RepositorioLibro
from controlador.controllerPaginaPrincipal import ControllerPaginaPrincipal

class PaginaPrincipalVista:
    def mostrar(repLib, usuario): ###
        limpiar_pantalla()
        print(f"Hola {usuario.nombre}, bienvenido a la biblioteca.")
        print("\nLista de Libros:")
        libros = repLib.listarLibros()
        for libro in libros:
            print(f"- {libro}")
        print("\nLibros prestados:")
        if len(usuario.librosPrestados) == 0:
            print("No se ha realizado ningún préstamo aún.")
        else:
            print(usuario.imprimirLibrosPrestados())
        print("\n¿Qué deseas hacer?")
        print("[1] Prestar un libro.\n[2] Devolver un libro.\n[3] Salir")
        accionUsuario = input()
        #controller.cambiarVentana(accionUsuario)
        return accionUsuario 
        