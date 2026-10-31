# Tarea U3: listas de pasajeros

Implementación de la guía del HTML con los ocho ejercicios en archivos independientes.
Requiere Python 3 y no necesita instalar paquetes.

## Listas de pasajeros

Los archivos `pasajero.py`, `lista_manual.py`, `lista_python.py` y `main.py`
están dentro de `tarea_listas/`. La clase `Pasajero` conserva el código de la guía.

Desde la raíz del repositorio, entra en la carpeta del proyecto y ejecuta:

```bash
cd tarea_listas
python main.py
```

En el menú principal, `1` abre la lista manual, `2` la lista de Python y `3` sale.
Cada lista tiene las opciones 1 a 15, `C` para cargar los cinco pasajeros de prueba
y `0` para volver. Las posiciones empiezan en cero.

La búsqueda binaria requiere ordenar primero por cédula con la opción `9`.
La lista manual tiene capacidad para diez pasajeros; la lista de Python crece
según los datos añadidos. Ambas rechazan cédulas duplicadas.

## Archivos del proyecto

- [pasajero.py](tarea_listas/pasajero.py): clase de datos.
- [lista_manual.py](tarea_listas/lista_manual.py): lista construida con índices y bucles.
- [lista_python.py](tarea_listas/lista_python.py): lista con métodos de Python.
- [main.py](tarea_listas/main.py): menú de las dos listas.

Los ocho ejercicios están separados en la misma carpeta, como se indica en la tabla siguiente.

## Ejercicios separados

| Archivo | Ejercicio | Ejecución |
| --- | --- | --- |
| [ejercicio1.py](tarea_listas/ejercicio1.py) | CRUD de pasajeros y orden por nombre | `python ejercicio1.py` |
| [ejercicio2.py](tarea_listas/ejercicio2.py) | Estadísticas de notas | `python ejercicio2.py` |
| [ejercicio3.py](tarea_listas/ejercicio3.py) | Burbuja y ordenamiento de Python | `python ejercicio3.py` |
| [ejercicio4.py](tarea_listas/ejercicio4.py) | Contar apariciones | `python ejercicio4.py` |
| [ejercicio5.py](tarea_listas/ejercicio5.py) | Invertir una lista | `python ejercicio5.py` |
| [ejercicio6.py](tarea_listas/ejercicio6.py) | Únicos conservando el orden | `python ejercicio6.py` |
| [ejercicio7.py](tarea_listas/ejercicio7.py) | Segundo mayor distinto | `python ejercicio7.py` |
| [ejercicio8.py](tarea_listas/ejercicio8.py) | Fusionar listas ordenadas | `python ejercicio8.py` |

Cada archivo usa una función y llamadas directas, con los datos del HTML.
Las versiones manual y de Python se muestran cuando las pide el enunciado.

## Comprobación de la guía

- `lista_manual.py` implementa los métodos con índices, bucles y variables auxiliares.
- `lista_python.py` incluye las cinco comprensiones obligatorias, la alternativa
  con `remove` comentada y el número de líneas de cada método manual.
- Las respuestas sobre `key`, copia superficial y complejidad de `insert`
  están en comentarios de `ordenar_asc`, `copiar` e `insertar`, respectivamente.
- Los docstrings originales describen los procesos, bosquejos y pruebas de cada método.

Para comparar ambas listas, ejecuta en cada una la secuencia de la Fase 4:
`C → 9 → 5 (0923456789) → 12 → 14 → 15 → 8 (0987654321) → 7 (0) → 2`.
Para probar duplicados, carga `C` dos veces: deben quedar cinco pasajeros.

La copia superficial permite invertir el orden de la copia sin cambiar el original.
Los objetos Pasajero sí se comparten entre ambas listas, como explica la guía.
