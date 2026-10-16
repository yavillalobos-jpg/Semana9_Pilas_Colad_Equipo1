# Semana 9: pilas y colas

Prácticas introductorias de estructuras de datos, hechas con Python básico. Los programas no importan módulos ni usan bibliotecas externas. Para simplificar la cola, se usa una lista: `append()` agrega al final y `pop(0)` retira el primer elemento.

## Archivos

- `pila_guiada.py`: agrega y retira libros con una pila LIFO.
- `reto1_bodega.py`: controla las cajas de la bodega con un menú y muestra una pila de cinco cajas.
- `pila_acciones.py`: guarda acciones pendientes y deshace la última.
- `reto2_navegador.py`: visita páginas, consulta la actual y regresa a páginas anteriores.
- `cola_guiada.py`: registra y atiende pacientes con una cola FIFO.
- `reto3_atencion.py`: registra turnos de clientes, atiende en orden y muestra la fila.
- `evidencias/simulacion_pila.png` y `evidencias/simulacion_cola.png`: salidas de las simulaciones ejecutadas.
- `evidencias/pruebas/`: registro de las pruebas realizadas.

## Cómo ejecutar

Abre una terminal en esta carpeta y ejecuta, por ejemplo:

```text
python pila_guiada.py
python reto1_bodega.py
python pila_acciones.py
python reto2_navegador.py
python cola_guiada.py
python reto3_atencion.py
```

Cada programa presenta una demostración o prueba y después abre su menú interactivo. Usa `Ctrl+C` si necesitas finalizar la ejecución desde la terminal.

## Cómo funcionan

- **Pila (LIFO):** el último elemento agregado es el primero que se retira. En Python, `append()` agrega arriba y `pop()` retira el elemento del tope.
- **Cola (FIFO):** el primer elemento agregado es el primero que se atiende. Aquí se agrega con `append()` y se atiende con `pop(0)`.
- En el navegador, las páginas anteriores se guardan en una pila. La página actual no se incluye en esa pila hasta que se visita otra página.
- Las operaciones se separan en funciones para que cada una tenga una tarea concreta. Los menús comprueban las opciones y las funciones revisan si la estructura está vacía antes de retirar elementos.

## Pruebas incluidas

- `pila_guiada.py`: agrega tres libros, muestra el tope, retira el último libro y vuelve a mostrar la pila.
- `reto1_bodega.py`: agrega cinco códigos distintos y representa las cajas una encima de otra.
- `pila_acciones.py`: registra acciones, consulta el historial y deshace acciones, incluso cuando ya no queda ninguna.
- `reto2_navegador.py`: visita `uam.edu.ni`, `python.org` y `github.com`; al regresar muestra `python.org`, luego `uam.edu.ni` y finalmente `No existen páginas anteriores.`
- `cola_guiada.py`: registra a Ana, Luis y María; atiende primero a Ana.
- `reto3_atencion.py`: registra cinco clientes, muestra la cantidad pendiente y permite atenderlos en orden FIFO.
- En cada menú se pueden probar entradas vacías, operaciones con la pila o cola vacía y opciones no válidas.

Las dos imágenes de `evidencias/` muestran salidas obtenidas al ejecutar los programas con entradas de prueba; el registro de validaciones está en `evidencias/pruebas/README.md`. Si el docente solicita capturas tomadas directamente del escritorio, vuelve a ejecutar cada programa en una terminal y reemplázalas por esas capturas. Los nombres de integrantes de abajo fueron facilitados para completar el README.

## Integrantes

- Litzy Mendoza
- Camila Vallejos
- Yader Villalobos

## Conceptos en pocas palabras

`append(elemento)` agrega un elemento al final de una lista. `pop()` sin posición quita y devuelve el último elemento, por eso funciona para una pila. `pop(0)` quita y devuelve el elemento que está en la posición cero, por eso esta práctica lo usa para atender una cola en orden de llegada.
