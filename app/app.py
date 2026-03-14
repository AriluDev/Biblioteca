from modelo.entidad.libro import Libro
from modelo.entidad.usuario import Usuario
from modelo.entidad.membresia import Membresia
from modelo.repositorio.repositorioLibro import RepositorioLibro
from modelo.repositorio.repositorioUsuario import RepositorioUsuario
from modelo.repositorio.repositorioMembresia import RepositorioMembresia
from modelo.repositorio.repositorioPrestamo import RepositorioPrestamo
from modelo.servicios.login import Login
from modelo.servicios.asignarMembresia import AsignarMembresia
from modelo.servicios.prestarLibro import ServicioPrestarLibro
from controlador.controllerLogin import ControllerLogin
from controlador.controllerPaginaPrincipal import ControllerPaginaPrincipal
from vista.inicioSesion import InicioSesionVista
from vista.paginaPrincipal import PaginaPrincipalVista
from vista.prestamoVentana import PrestamoVentana

def iniciarSistema():
    pass

# Libros
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

repLib = RepositorioLibro()
repLib.agregarLibros(lib1, lib2, lib3, lib4, lib5, lib6, lib7, lib8, lib9, lib10)

# Usuarios
usu1 = Usuario("Ariel", "contraseña123")
usu2 = Usuario("Victoria", "contra123")
usu3 = Usuario("María", "secreto123")

repUsu = RepositorioUsuario()
repUsu.agregarUsuarios(usu1, usu2, usu3)

# Membresias
basica = Membresia("Básica", 5)
premium = Membresia("Premium", 10)
repMem = RepositorioMembresia()
repMem.agregarMembresias(basica, premium)
asignador = AsignarMembresia(repUsu, repMem)
asignador.asignarMembresia("Ariel", "Básica")
asignador.asignarMembresia("Victoria" , "Premium")
asignador.asignarMembresia("María" , "premium")

# Creación de ventanas
loginView = InicioSesionVista()
paginaPrincipalView = PaginaPrincipalVista()
prestamoView = PrestamoVentana()

#Creación de servicios
login = Login(repUsu)

# Creación de controller
loginController = ControllerLogin(login)
#paginaPrincipalController = ControllerPaginaPrincipal()

# Ciclo de la página
usuario = loginView.mostrar(loginController)
paginaPrincipalView.mostrar(repLib, usuario)

# Prestamos
repPre = RepositorioPrestamo()
prestarLibro = ServicioPrestarLibro(repUsu, repLib)
prestarLibro.prestarLibro("Ariel", "100 años de soledad", repPre)
prestarLibro.prestarLibro("Victoria", "100 años de soledad", repPre)
prestarLibro.prestarLibro("Ariel", "Drácula", repPre)
print(lib1)
print(usu1)
print(usu2)
print(repPre)