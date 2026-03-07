from modelo.entidad.libro import Libro

class RepositorioLibro:
    def __init__(self):
        self.__libros = []

    def agregarLibro(self, *libro: Libro):
        for i in self.__libros:
            if i.titulo == libro.titulo:
                raise Exception("El libro ya ha sido agregado anteriormente.")
        self.__libros.append(libro)

    def eliminarLibro(self, libro: Libro):
        for i in self.__libros:
            if i.titulo == libro.titulo:
                self.__libros.remove(i)
                return
        raise Exception("No existe el libro que se pretende eliminar.")

    def buscarPorAutor(self, autor):
        coincidencias = []
        for libro in self.__libros:
            if libro.autor == autor:
                coincidencias.append(libro)
        if len(coincidencias) > 0:
            return coincidencias
        raise Exception("No se encontró ningún libro del autor buscado.")

    def buscarPorTitulo(self, titulo):
        coincidencias = []
        for libro in self.__libros:
            if libro.titulo == titulo:
                coincidencias.append(libro)
        if len(coincidencias) > 0:
            return coincidencias
        raise Exception("No se encontró ningún libro con el título buscado.")

    def listarLibros(self):
        return self.__libros.copy()

    def listarLibrosDisponibles(self):
        return [libro for libro in self.__libros if libro.stock > 0]