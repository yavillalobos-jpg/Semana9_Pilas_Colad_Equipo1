cajas = []


def apilar_caja(codigo):
    codigo = codigo.strip()
    if not codigo:
        print("El código no puede estar vacío.")
    elif codigo in cajas:
        print("Ese código ya existe en la pila.")
    else:
        cajas.append(codigo)
        print(f"Caja agregada: {codigo}")


def retirar_caja():
    if not cajas:
        print("No se puede retirar: la pila está vacía.")
    else:
        codigo = cajas.pop()
        print(f"Caja retirada: {codigo}")


def consultar_tope():
    if not cajas:
        print("No hay cajas en la bodega.")
    else:
        print(f"Caja en el tope: {cajas[-1]}")


def mostrar_pila():
    if not cajas:
        print("La pila está vacía.")
        return

    ancho = max(11, max(len(codigo) for codigo in cajas))
    borde = "+" + "-" * (ancho + 2) + "+"
    print("Pilas de cajas (de arriba hacia abajo):")
    for codigo in reversed(cajas):
        print(f"   {borde}")
        print(f"   | {codigo:<{ancho}} |")
    print(f"   {borde}")
    print(f"Cantidad de cajas: {len(cajas)}")


def ejecutar_simulacion():
    print("=== Simulación de bodega (pila LIFO) ===")
    for codigo in ["CAJA-01", "CAJA-02", "CAJA-03", "CAJA-04", "CAJA-05"]:
        apilar_caja(codigo)
    mostrar_pila()
    print("La simulación deja cinco cajas listas para probar el menú.\n")


def menu():
    while True:
        print("=== Control de cajas en bodega ===")
        print("1. Apilar caja")
        print("2. Desapilar caja")
        print("3. Consultar tope")
        print("4. Mostrar pila")
        print("5. Mostrar cantidad")
        print("6. Salir")
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            apilar_caja(input("Código de la caja: "))
        elif opcion == "2":
            retirar_caja()
        elif opcion == "3":
            consultar_tope()
        elif opcion == "4":
            mostrar_pila()
        elif opcion == "5":
            print(f"Cantidad de cajas: {len(cajas)}")
        elif opcion == "6":
            print("Programa terminado.")
            break
        else:
            print("Opción no válida. Elija del 1 al 6.")
        print()


ejecutar_simulacion()
menu()
