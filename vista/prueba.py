def login():
    print("===== BIENVENIDO A LA BIBLIOTECA =====")
    usuario = input("Ingrese su nombre de usuario: ")
    contrasena = input("Ingrese su contraseña: ")
    print("\nInicio de sesión correcto. Bienvenido", usuario)
    return usuario


def mostrar_libros(libros):
    print("\nLibros disponibles en la biblioteca:")
    for libro in libros:
        print("-", libro)


def adquirir_libro(libros, libros_prestados):
    print("\n¿Qué libro desea adquirir?")
    for libro in libros:
        print("-", libro)

    libro = input("Escriba el nombre del libro: ")

    if libro in libros:
        libros.remove(libro)
        libros_prestados.append(libro)
        print("Has adquirido el libro:", libro)
    else:
        print("Ese libro no está disponible.")


def devolver_libro(libros, libros_prestados):
    if len(libros_prestados) == 0:
        print("\nNo tienes libros prestados.")
        return

    print("\nLibros que tienes prestados:")
    for libro in libros_prestados:
        print("-", libro)

    libro = input("¿Qué libro deseas devolver?: ")

    if libro in libros_prestados:
        libros_prestados.remove(libro)
        libros.append(libro)
        print("Libro devuelto correctamente.")
    else:
        print("No tienes ese libro.")


def menu():
    print("\n===== MENÚ =====")
    print("1. Ver libros disponibles")
    print("2. Adquirir un libro")
    print("3. Devolver un libro")
    print("4. Salir")


#PROGRAMA PRINCIPAL

libros = [
    "Don Quijote de la Mancha",
    "Cien años de soledad",
    "El Principito",
    "Harry Potter",
    "La Odisea"
]

libros_prestados = []

usuario = login()

while True:
    menu()
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        mostrar_libros(libros)

    elif opcion == "2":
        adquirir_libro(libros, libros_prestados)

    elif opcion == "3":
        devolver_libro(libros, libros_prestados)

    elif opcion == "4":
        print("Gracias por usar la biblioteca.")
        break

    else:
        print("Opción no válida.")