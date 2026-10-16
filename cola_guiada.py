from collections import deque

cola = deque()


def registrar_paciente(nombre):
    nombre = nombre.strip()
    if not nombre:
        print("El nombre no puede estar vacío.")
    else:
        cola.append(nombre)
        print(f"Registrado: {nombre}")


def atender_paciente():
    if not cola:
        print("No hay pacientes en espera.")
    else:
        paciente = cola.popleft()
        print(f"Atendiendo a: {paciente}")


def mostrar_cola():
    if not cola:
        print("La cola está vacía.")
    else:
        print("Pacientes en espera:")
        for posicion, paciente in enumerate(cola, start=1):
            print(f"{posicion}. {paciente}")


def ejecutar_demostracion():
    print("=== Demostración de cola FIFO ===")
    registrar_paciente("Ana")
    registrar_paciente("Luis")
    registrar_paciente("María")
    mostrar_cola()
    atender_paciente()
    mostrar_cola()
    print(
        "FIFO atiende primero a quien llegó primero; "
        "con una pila se atendería primero a quien llegó al final."
    )
    print("La demostración terminó.\n")


def menu():
    while True:
        print("=== Mi primera cola ===")
        print("1. Registrar paciente")
        print("2. Atender paciente")
        print("3. Mostrar pacientes en espera")
        print("4. Salir")
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            registrar_paciente(input("Nombre del paciente: "))
        elif opcion == "2":
            atender_paciente()
        elif opcion == "3":
            mostrar_cola()
        elif opcion == "4":
            print("Programa terminado.")
            break
        else:
            print("Opción no válida. Elija del 1 al 4.")
        print()


ejecutar_demostracion()
menu()