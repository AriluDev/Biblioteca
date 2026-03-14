class Usuario:
    def __init__(self, nombre, contrasena):
        self.__nombre = nombre
        self.__contrasena = contrasena
        self.__membresia = None
        self.__librosPrestados = []
    
    def __str__(self):
        return f"Nombre: {self.nombre} - Membresía: {self.membresia} - Préstamos: {self.__imprimirLibrosPrestados()}"

    def __repr__(self):
        return self.__str__()
    
    def agregarPrestamo(self, prestamo: "Prestamo"):
        self.__librosPrestados.append(prestamo.libro)

    def quitarPrestamo(self, libro):
        self.__librosPrestados.remove(libro)

    def __imprimirLibrosPrestados(self):
            return ", ".join(str(libro.titulo) for libro in self.__librosPrestados)

    @property
    def nombre(self):
        return self.__nombre
    
    @property
    def contrasena(self):
        return self.__contrasena

    @property
    def membresia(self):
        return self.__membresia
    
    @property
    def librosPrestados(self):
        return self.__librosPrestados
    
    @membresia.setter
    def membresia(self, membresia):
        self.__membresia = membresia