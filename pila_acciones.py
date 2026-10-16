acciones = []


def registrar_accion(descripcion):
    descripcion = descripcion.strip()
    if not descripcion:
        print("La descripción no puede estar vacía.")
    else:
        acciones.append(descripcion)
        print(f"Acción registrada: {descripcion}")


def deshacer():
    if not acciones:
        print("No existen acciones para deshacer.")
    else:
        ultima = acciones.pop()
        print(f"Se deshizo: {ultima}")


def historial():
    if not acciones:
        print("No hay acciones pendientes.")
    else:
        print("Acciones pendientes (de la más antigua a la más nueva):")
        for posicion, accion in enumerate(acciones, start=1):
            print(f"{posicion}. {accion}")
    print(f"Cantidad de acciones pendientes: {len(acciones)}")


def ejecutar_prueba():
    print("=== Prueba de deshacer acciones ===")
    registrar_accion("Escribir título")
    registrar_accion("Agregar párrafo")
    registrar_accion("Cambiar formato")
    historial()
    deshacer()
    historial()
    registrar_accion("Insertar imagen")
    deshacer()
    deshacer()
    deshacer()
    deshacer()
    print("La prueba incluye registros, historial y deshacer con pila vacía.\n")


def menu():
    while True:
        print("=== Editor: deshacer acciones ===")
        print("1. Registrar acción")
        print("2. Deshacer última acción")
        print("3. Mostrar historial")
        print("4. Mostrar cantidad pendiente")
        print("5. Salir")
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            registrar_accion(input("Descripción de la acción: "))
        elif opcion == "2":
            deshacer()
        elif opcion == "3":
            historial()
        elif opcion == "4":
            print(f"Cantidad de acciones pendientes: {len(acciones)}")
        elif opcion == "5":
            print("Programa terminado.")
            break
        else:
            print("Opción no válida. Elija del 1 al 5.")
        print()


ejecutar_prueba()
menu()
