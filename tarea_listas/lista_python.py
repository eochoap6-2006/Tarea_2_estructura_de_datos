from bisect import bisect_left
from pasajero import Pasajero

class ListaPasajerosPython:

    # CREAR
    def __init__(self):
        self.pasajeros = []

    # AÑADIR
    def añadir(self, pasajero):
        if self.buscar(pasajero.cedula) != -1:
            print(pasajero.cedula, "ya existe")
            return False
        self.pasajeros.append(pasajero)
        return True

    # LISTAR
    def listar(self):
        if not self.pasajeros:
            print("Lista vacía")
            return
        for i, p in enumerate(self.pasajeros):
            print(f"[{i}] {p}")

    # LONGITUD (manual: 1 línea)
    def longitud(self):
        return len(self.pasajeros)

    # INSERTAR (manual: 16 líneas)
    def insertar(self, posicion, pasajero):
        if posicion < 0 or posicion > len(self.pasajeros):
            print("Posición no válida")
            return False
        if self.buscar(pasajero.cedula) != -1:
            print(pasajero.cedula, "ya existe")
            return False

        # insert desplaza elementos: O(n).
        self.pasajeros.insert(posicion, pasajero)
        return True

    # BUSCAR (manual: 4 líneas)
    def buscar(self, cedula):
        posiciones = [i for i, p in enumerate(self.pasajeros) if p.cedula == cedula]
        if not posiciones:
            return -1
        return posiciones[0]

    # BUSCAR BINARIA: lista ordenada (manual: 11 líneas)
    def buscar_binaria(self, cedula):
        cedulas = [p.cedula for p in self.pasajeros]
        i = bisect_left(cedulas, cedula)
        if i < len(cedulas) and cedulas[i] == cedula:
            return i
        return -1

    # MODIFICAR (manual: 10 líneas)
    def modificar(self, cedula, nuevo_nombre, nueva_edad):
        pos = self.buscar(cedula)
        if pos == -1:
            print(cedula, "no existe")
            return False
        if not nuevo_nombre.strip() or nueva_edad < 0:
            print("Nombre o edad no válidos")
            return False
        self.pasajeros[pos].nombre = nuevo_nombre
        self.pasajeros[pos].edad = nueva_edad
        return True

    # ELIMINAR POR POSICIÓN (manual: 9 líneas)
    def eliminar_por_posicion(self, posicion):
        if posicion < 0 or posicion >= len(self.pasajeros):
            print("Posición no válida")
            return None
        return self.pasajeros.pop(posicion)

    # ELIMINAR POR VALOR (manual: 6 líneas)
    def eliminar_por_valor(self, cedula):
        # pos = self.buscar(cedula)
        # if pos != -1:
        #     self.pasajeros.remove(self.pasajeros[pos])
        # return pos != -1

        antes = len(self.pasajeros)
        self.pasajeros = [p for p in self.pasajeros if p.cedula != cedula]
        if len(self.pasajeros) == antes:
            print(cedula, "no existe")
        return len(self.pasajeros) < antes

    # ORDENAR ASCENDENTE (manual: 7 líneas)
    def ordenar_asc(self):
        # key compara cédulas; sin key, ordenar Pasajero produce TypeError.
        self.pasajeros.sort(key=lambda p: p.cedula)

    # ORDENAR DESCENDENTE (manual: 7 líneas)
    def ordenar_desc(self):
        self.pasajeros.sort(key=lambda p: p.cedula, reverse=True)

    # REVERSAR (manual: 8 líneas)
    def reversar(self):
        self.pasajeros.reverse()

    # COPIAR (manual: 4 líneas)
    def copiar(self):
        nueva = ListaPasajerosPython()

        # Orden independiente; pasajeros compartidos: modificarlos afecta al original.
        nueva.pasajeros = self.pasajeros.copy()
        return nueva

    # FILTRAR MAYORES DE EDAD (manual: 5 líneas)
    def filtrar_mayores_de_edad(self):
        nueva = ListaPasajerosPython()
        nueva.pasajeros = [p for p in self.pasajeros if p.es_mayor_de_edad()]
        return nueva

    # NOMBRES EN MAYÚSCULAS (manual: 4 líneas)
    def nombres_en_mayusculas(self):
        return [p.nombre.upper() for p in self.pasajeros]

