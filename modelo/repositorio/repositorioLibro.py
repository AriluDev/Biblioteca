from modelo.entidad.libro import Libro

class RepositorioLibro:
    def __init__(self):
        self.__libros = []

    def __str__(self):
        return self.__libros
    
    def __repr__(self):
        return self.__str__()

    def agregarLibros(self, *libros: Libro):
        coincidencias = []

        for libro in libros:
            if any(libro.titulo == existente.titulo for existente in self.__libros):
                coincidencias.append(libro)
            else:
                self.__libros.append(libro)

        if coincidencias:
            print(f"Los siguientes libros no han sido agregados porque ya existen: {coincidencias}")
    
    def eliminarLibros(self, *libros: Libro):
        coincidencias = []

        for libro in libros:
            if any(libro.titulo == existente.titulo for existente in self.__libros):
                self.__libros.remove(libro)
            else:
                coincidencias.append(libro)
        
        if coincidencias:
            print(f"Los siguientes libros no han sido eliminados porque no existen: {coincidencias}")

    def buscarPorAutor(self, autor):
        coincidencias = []
        for libro in self.__libros:
            if libro.autor == autor:
                coincidencias.append(libro)
        if len(coincidencias) > 0:
            return coincidencias
        raise Exception("No se encontró ningún libro del autor buscado.")

    def buscarPorTitulo(self, titulo):
        for libro in self.__libros:
            if libro.titulo == titulo:
                return libro
        raise Exception("No se encontró ningún libro con el título buscado.")

    def listarLibros(self):
        return self.__libros.copy()

    def listarLibrosDisponibles(self):
        return [libro for libro in self.__libros if libro.stock > 0]