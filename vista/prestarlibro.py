from vista import limpiar_pantalla
from modelo.repositorio.repositorioLibro import RepositorioLibro

class prestarLibro:
    def ventanaPrestarLibro():
        limpiar_pantalla() 
        print("\nPrestamo de libros") 
        nombreLibro = input("Escriba el nombre del libro que deseas pedir prestado: ")
        return nombreLibro