historial_atras = []
pagina_actual = None


def visitar_pagina(url):
    global pagina_actual
    url = url.strip()
    if not url:
        print("La dirección no puede estar vacía.")
        return

    if pagina_actual is not None:
        historial_atras.append(pagina_actual)
    pagina_actual = url
    print(f"Página actual: {pagina_actual}")


def regresar():
    global pagina_actual
    if not historial_atras:
        print("No existen páginas anteriores.")
    else:
        pagina_actual = historial_atras.pop()
        print(f"Página actual: {pagina_actual}")


def consultar_pagina():
    if pagina_actual is None:
        print("No hay una página abierta.")
    else:
        print(f"Página actual: {pagina_actual}")


def mostrar_historial():
    if not historial_atras:
        print("No hay páginas anteriores en el historial.")
    else:
        print("Páginas anteriores, de la más antigua a la más reciente:")
        for pagina in historial_atras:
            print(f"- {pagina}")
    print(f"Cantidad de páginas anteriores: {len(historial_atras)}")


def ejecutar_prueba_obligatoria():
    print("=== Prueba obligatoria de navegación ===")
    visitar_pagina("uam.edu.ni")
    visitar_pagina("python.org")
    visitar_pagina("github.com")
    regresar()
    regresar()
    regresar()
    print()


def menu():
    while True:
        print("=== Historial de navegación ===")
        print("1. Visitar una página nueva")
        print("2. Regresar a la página anterior")
        print("3. Consultar página actual")
        print("4. Mostrar historial pendiente de retroceso")
        print("5. Mostrar cantidad de páginas anteriores")
        print("6. Salir")
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            visitar_pagina(input("Dirección de la página: "))
        elif opcion == "2":
            regresar()
        elif opcion == "3":
            consultar_pagina()
        elif opcion == "4":
            mostrar_historial()
        elif opcion == "5":
            print(f"Cantidad de páginas anteriores: {len(historial_atras)}")
        elif opcion == "6":
            print("Programa terminado.")
            break
        else:
            print("Opción no válida. Elija del 1 al 6.")
        print()


ejecutar_prueba_obligatoria()
menu()
