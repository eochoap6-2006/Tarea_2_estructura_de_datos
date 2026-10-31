# =====================================================================
#  lista_python.py  —  LISTA 2: con el list de PYTHON (built-in)
# ---------------------------------------------------------------------
#  Mismas operaciones que la Lista 1, pero ahora usamos lo que Python
#  ya trae: append, insert, pop, remove, sort, reverse, copy, len,
#  enumerate, next, bisect ... y LIST COMPREHENSIONS.
#
#      self.pasajeros -> [Pasajero, Pasajero, ...]   (crece sola)
#
#  ✅ OBLIGATORIO usar comprensiones de listas en (mínimo):
#       buscar · buscar_binaria · eliminar_por_valor (versión 2)
#       filtrar_mayores_de_edad · nombres_en_mayusculas
#
#  Recordatorio de la sintaxis:
#       [EXPRESIÓN for ELEMENTO in LISTA]            -> transformar
#       [ELEMENTO  for ELEMENTO in LISTA if COND]    -> filtrar
#       [EXPRESIÓN for ELEMENTO in LISTA if COND]    -> las dos a la vez
#
#  📌 Compara cada método con su gemelo de lista_manual.py:
#     allá eran 10 líneas, aquí casi siempre son 1 o 2.
#  Los métodos están completados según los pasos de la guía.
# =====================================================================

from bisect import bisect_left
from pasajero import Pasajero


class ListaPasajerosPython:

    def __init__(self):
        self.pasajeros = []               # list de Python: crece sola

    # -----------------------------------------------------------------
    # 1. AÑADIR  ✅ YA RESUELTO
    # -----------------------------------------------------------------
    def añadir(self, pasajero):
        """Añade al final con append()."""
        if self.buscar(pasajero.cedula) != -1:
            print("⚠ Ya existe un pasajero con esa cédula")
            return False
        self.pasajeros.append(pasajero)
        return True

    # -----------------------------------------------------------------
    # 2. LISTAR  ✅ YA RESUELTO
    # -----------------------------------------------------------------
    def listar(self):
        """Muestra los pasajeros con su posición usando enumerate()."""
        if not self.pasajeros:                  # lista vacía es False
            print("(lista vacía)")
            return
        for i, p in enumerate(self.pasajeros):
            print(f"[{i}] {p}")

    # -----------------------------------------------------------------
    # 3. LONGITUD
    # -----------------------------------------------------------------
    def longitud(self):
        """
        USA      : len()
        RETORNA  : int.   PRUEBA: datos de prueba -> 5
        """
        # Versión manual: 1 línea de código (sin def, docstring ni comentarios).
        return len(self.pasajeros)

    # -----------------------------------------------------------------
    # 4. INSERTAR
    # -----------------------------------------------------------------
    def insertar(self, posicion, pasajero):
        """
        USA      : self.pasajeros.insert(posicion, pasajero)
        VALIDA   : 0 <= posicion <= len(self.pasajeros); si no, mensaje y False.
        PIENSA   : ¿por qué ya no tienes que correr nada a la derecha?
                   (Python lo hace por ti... pero lo sigue haciendo: O(n)).
        """
        # Versión manual: 16 líneas de código (sin def, docstring ni comentarios).
        if posicion < 0 or posicion > len(self.pasajeros):
            print("Posición no válida")
            return False
        if self.buscar(pasajero.cedula) != -1:
            print("⚠ Ya existe un pasajero con esa cédula")
            return False
        # Python desplaza los elementos a la derecha para abrir el espacio.
        # Insertar al principio cuesta O(n), aunque se escriba en una línea.
        self.pasajeros.insert(posicion, pasajero)
        return True

    # -----------------------------------------------------------------
    # 5. BUSCAR POR CÉDULA  (con COMPRENSIÓN)
    # -----------------------------------------------------------------
    def buscar(self, cedula):
        """
        RETORNA  : la posición (int) o -1.
        USA      : una comprensión con enumerate que junte las posiciones
                   que coinciden:
                       posiciones = [i for i, p in enumerate(self.pasajeros)
                                     if p.cedula == cedula]
                   Si la lista 'posiciones' está vacía -> -1,
                   si no -> posiciones[0].
        EXTRA    : investiga la versión con next(...):
                   next((i for i, p in enumerate(...) if ...), -1)
        PRUEBA   : buscar("0987654321") -> 2 ;  buscar("1111111111") -> -1
        """
        # Versión manual: 4 líneas de código (sin def, docstring ni comentarios).
        posiciones = [i for i, p in enumerate(self.pasajeros) if p.cedula == cedula]
        if not posiciones:
            return -1
        return posiciones[0]

    # -----------------------------------------------------------------
    # 6. BUSCAR BINARIA  (con COMPRENSIÓN + bisect)
    # -----------------------------------------------------------------
    def buscar_binaria(self, cedula):
        """
        ⚠ REQUISITO: lista ordenada por cédula (ordenar_asc antes).
        PASOS    :
          1. cedulas = [p.cedula for p in self.pasajeros]   # COMPRENSIÓN
          2. i = bisect_left(cedulas, cedula)   # dónde "debería" estar
          3. Si i < len(cedulas) y cedulas[i] == cedula -> return i
          4. return -1
        PRUEBA   : datos ordenados -> buscar_binaria("0923456789") -> 2
        """
        # Versión manual: 11 líneas de código (sin def, docstring ni comentarios).
        cedulas = [p.cedula for p in self.pasajeros]
        i = bisect_left(cedulas, cedula)
        if i < len(cedulas) and cedulas[i] == cedula:
            return i
        return -1

    # -----------------------------------------------------------------
    # 7. MODIFICAR
    # -----------------------------------------------------------------
    def modificar(self, cedula, nuevo_nombre, nueva_edad):
        """
        PASOS    : pos = self.buscar(cedula); si -1 -> False;
                   si no, cambia self.pasajeros[pos].nombre y .edad -> True
        """
        # Versión manual: 10 líneas de código (sin def, docstring ni comentarios).
        pos = self.buscar(cedula)
        if pos == -1:
            print("El pasajero no existe")
            return False
        if not nuevo_nombre.strip() or nueva_edad < 0:
            print("Nombre o edad no válidos")
            return False
        self.pasajeros[pos].nombre = nuevo_nombre
        self.pasajeros[pos].edad = nueva_edad
        return True

    # -----------------------------------------------------------------
    # 8. ELIMINAR POR POSICIÓN
    # -----------------------------------------------------------------
    def eliminar_por_posicion(self, posicion):
        """
        USA      : self.pasajeros.pop(posicion)   (retorna el eliminado)
        VALIDA   : 0 <= posicion < len(...); si no -> mensaje y None
        """
        # Versión manual: 9 líneas de código (sin def, docstring ni comentarios).
        if posicion < 0 or posicion >= len(self.pasajeros):
            print("Posición no válida")
            return None
        return self.pasajeros.pop(posicion)

    # -----------------------------------------------------------------
    # 9. ELIMINAR POR VALOR (por cédula)  — hazlo de DOS formas
    # -----------------------------------------------------------------
    def eliminar_por_valor(self, cedula):
        """
        FORMA 1 (remove):
            pos = self.buscar(cedula) ... self.pasajeros.remove(self.pasajeros[pos])
        FORMA 2 (COMPRENSIÓN) — la que debe quedar activa:
            antes = len(self.pasajeros)
            self.pasajeros = [p for p in self.pasajeros if p.cedula != cedula]
            return len(self.pasajeros) < antes      # True si eliminó algo
        Deja la FORMA 1 comentada para comparar.
        """
        # Versión manual: 6 líneas de código (sin def, docstring ni comentarios).
        # FORMA 1 (remove), comentada para comparar:
        # pos = self.buscar(cedula)
        # if pos == -1:
        #     print("El pasajero no existe")
        #     return False
        # self.pasajeros.remove(self.pasajeros[pos])
        # return True

        antes = len(self.pasajeros)
        self.pasajeros = [p for p in self.pasajeros if p.cedula != cedula]
        if len(self.pasajeros) == antes:
            print("El pasajero no existe")
        return len(self.pasajeros) < antes

    # -----------------------------------------------------------------
    # 10. ORDENAR ASCENDENTE (por cédula)
    # -----------------------------------------------------------------
    def ordenar_asc(self):
        """
        USA      : self.pasajeros.sort(key=lambda p: p.cedula)
        PIENSA   : ¿qué hace key=? ¿qué pasaría sin él? (pruébalo)
        """
        # Versión manual: 7 líneas de código (sin def, docstring ni comentarios).
        # key extrae la cédula: sort compara los textos de las cédulas.
        # Sin key se produce TypeError, porque Pasajero no define la comparación <.
        self.pasajeros.sort(key=lambda p: p.cedula)

    # -----------------------------------------------------------------
    # 11. ORDENAR DESCENDENTE (por cédula)
    # -----------------------------------------------------------------
    def ordenar_desc(self):
        """ USA : sort(key=..., reverse=True) """
        # Versión manual: 7 líneas de código (sin def, docstring ni comentarios).
        self.pasajeros.sort(key=lambda p: p.cedula, reverse=True)

    # -----------------------------------------------------------------
    # 12. REVERSAR
    # -----------------------------------------------------------------
    def reversar(self):
        """ USA : self.pasajeros.reverse()   (no es lo mismo que ordenar_desc) """
        # Versión manual: 8 líneas de código (sin def, docstring ni comentarios).
        self.pasajeros.reverse()

    # -----------------------------------------------------------------
    # 13. COPIAR
    # -----------------------------------------------------------------
    def copiar(self):
        """
        PASOS    :
          nueva = ListaPasajerosPython()
          nueva.pasajeros = self.pasajeros.copy()    # o self.pasajeros[:]
          return nueva
        ⚠ OJO    : es una copia SUPERFICIAL: las dos listas son distintas,
                   pero los objetos Pasajero de adentro son los MISMOS.
                   Reversar la copia no afecta al original;
                   modificar un pasajero de la copia... ¡sí! Pruébalo.
        """
        # Versión manual: 4 líneas de código (sin def, docstring ni comentarios).
        nueva = ListaPasajerosPython()
        # Es una copia superficial: otra lista con los mismos objetos Pasajero.
        # Reversar la copia cambia su orden y deja intacto el orden del original.
        # Modificar un pasajero de la copia también cambia lo visto en el original,
        # porque ambas listas contienen una referencia al mismo pasajero.
        nueva.pasajeros = self.pasajeros.copy()
        return nueva

    # -----------------------------------------------------------------
    # 14. FILTRAR MAYORES DE EDAD  (COMPRENSIÓN que FILTRA)
    # -----------------------------------------------------------------
    def filtrar_mayores_de_edad(self):
        """
        RETORNA  : una NUEVA ListaPasajerosPython.
        PASOS    :
          nueva = ListaPasajerosPython()
          nueva.pasajeros = [p for p in self.pasajeros if p.es_mayor_de_edad()]
          return nueva
        PRUEBA   : datos de prueba -> todos menos Beto
        """
        # Versión manual: 5 líneas de código (sin def, docstring ni comentarios).
        nueva = ListaPasajerosPython()
        nueva.pasajeros = [p for p in self.pasajeros if p.es_mayor_de_edad()]
        return nueva

    # -----------------------------------------------------------------
    # 15. NOMBRES EN MAYÚSCULAS  (COMPRENSIÓN que TRANSFORMA)
    # -----------------------------------------------------------------
    def nombres_en_mayusculas(self):
        """
        RETORNA  : list de str ->  [p.nombre.upper() for p in self.pasajeros]
        PRUEBA   : ['DIANA', 'ANA', 'LUIS', 'BETO', 'ELENA']
        """
        # Versión manual: 4 líneas de código (sin def, docstring ni comentarios).
        return [p.nombre.upper() for p in self.pasajeros]
