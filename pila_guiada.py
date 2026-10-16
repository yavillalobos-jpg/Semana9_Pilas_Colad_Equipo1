libros = []


def apilar(libro):
    libros.append(libro)
    print(f"Libro agregado: {libro}")


def desapilar():
    if not libros:
        print("La pila está vacía.")
    else:
        libro = libros.pop()
        print(f"Libro retirado: {libro}")


def mostrar_pila():
    if not libros:
        print("No hay libros.")
    else:
        print("Pila actual (base -> tope):", libros)
        print("Libro en el tope:", libros[-1])


def ejecutar_demostracion():
    print("=== Demostración de pila LIFO ===")
    apilar("Matemáticas")
    apilar("Programación")
    apilar("Base de Datos")
    mostrar_pila()
    desapilar()
    mostrar_pila()
    print("La demostración terminó.\n")


def menu():
    while True:
        print("=== Mi primera pila ===")
        print("1. Agregar libro")
        print("2. Retirar libro")
        print("3. Mostrar pila")
        print("4. Salir")
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            libro = input("Nombre del libro: ").strip()
            if libro:
                apilar(libro)
            else:
                print("El nombre no puede estar vacío.")
        elif opcion == "2":
            desapilar()
        elif opcion == "3":
            mostrar_pila()
        elif opcion == "4":
            print("Programa terminado.")
            break
        else:
            print("Opción no válida. Elija del 1 al 4.")
        print()


ejecutar_demostracion()
menu()
