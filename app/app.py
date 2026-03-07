from modelo.entidad.libro import Libro
from modelo.entidad.usuario import Usuario
from modelo.repositorio.repositorioLibro import RepositorioLibro
from modelo.entidad.prestamo import Prestamo
from modelo.entidad.prestamoDetalle import PrestamoDetalle

def iniciarSistema():
    pass

# Creando libros
lib1 = Libro("100 años de soledad", "Gabriel García Márquez")
lib2 = Libro("Drácula", "Bram Stoker")
lib3 = Libro("Frankstein", "Mary Shelley")
lib4 = Libro("La ciudad y los perros", "Mario Vargas Llosa")
lib5 = Libro("la tía Julia y el escribidor", "Mario Vargas Llosa")
lib6 = Libro("Los gremlins", "Roald Dahl")
lib7 = Libro("Matilda", "Roald Dahl")
lib8 = Libro("1984", "George Orwell")
lib9 = Libro("Rebelión en la granja", "George Orwell")
lib10 = Libro("La llamada de Cthulhu", "H. P. Lovecraft")

# Creando usuarios
usu1 = Usuario("Ariel", "contraseña123")
usu2 = Usuario("Victoria", "contra123")
usu3 = Usuario("José", "12345679")
usu4 = Usuario("Miguel", "987654321")
usu5 = Usuario("María", "secreto123")
usu6 = Usuario("Carla", "S_.12ñ")
usu7 = Usuario("María", "123seña123")

# Agregando libros al repositorio
rep = RepositorioLibro()
rep.agregarLibros(lib1, lib2, lib3, lib4, lib5, lib6, lib7, lib8, lib9, lib10)

# Generando prestámos
pres1 = Prestamo(usu1)
preDet1 = PrestamoDetalle(lib1, 2)
preDet2 = PrestamoDetalle(lib2, 1)
pres1.agregarDetalle(preDet1, preDet2)
print(pres1)
