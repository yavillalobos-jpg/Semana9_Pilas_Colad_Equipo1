from collections import deque

cola_clientes = deque()
siguiente_turno = 1


def registrar_cliente(nombre):
    global siguiente_turno
    nombre = nombre.strip()
    if not nombre:
        print("El nombre no puede estar vacío.")
    else:
        cliente = f"Turno {siguiente_turno} - {nombre}"
        cola_clientes.append(cliente)
        print(f"Cliente registrado: {cliente}")
        siguiente_turno += 1


def atender_cliente():
    if not cola_clientes:
        print("No hay clientes en espera.")
    else:
        cliente = cola_clientes.popleft()
        print(f"Atendiendo a: {cliente}")


def consultar_siguiente():
    if not cola_clientes:
        print("No hay clientes en espera.")
    else:
        print(f"Siguiente cliente: {cola_clientes[0]}")


def mostrar_clientes():
    if not cola_clientes:
        print("No hay clientes en espera.")
    else:
        print("Clientes en espera (primero en la fila al inicio):")
        for cliente in cola_clientes:
            print(f"  -> {cliente}")
    print(f"Cantidad de clientes pendientes: {len(cola_clientes)}")


def ejecutar_simulacion():
    print("=== Simulación del sistema de atención FIFO ===")
    for nombre in ["Ana", "Luis", "María", "Carlos", "Sofía"]:
        registrar_cliente(nombre)
    mostrar_clientes()
    print("En la fila, el primer cliente registrado debe ser el primero atendido.\n")


def menu():
    while True:
        print("=== Sistema de atención al cliente ===")
        print("1. Registrar cliente")
        print("2. Atender siguiente cliente")
        print("3. Consultar siguiente cliente")
        print("4. Mostrar clientes en espera")
        print("5. Mostrar cantidad pendiente")
        print("6. Salir")
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            registrar_cliente(input("Nombre del cliente: "))
        elif opcion == "2":
            atender_cliente()
        elif opcion == "3":
            consultar_siguiente()
        elif opcion == "4":
            mostrar_clientes()
        elif opcion == "5":
            print(f"Cantidad de clientes pendientes: {len(cola_clientes)}")
        elif opcion == "6":
            print("Programa terminado.")
            break
        else:
            print("Opción no válida. Elija del 1 al 6.")
        print()


ejecutar_simulacion()
menu()