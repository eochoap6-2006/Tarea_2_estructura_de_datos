def ejercicio_t1():
    """
    T1 — CRUD de pasajeros con clase Pasajero + list   (Taller, Medio)
    -----------------------------------------------------------------
    Demuestra (sin menú, con llamadas directas) el CRUD completo usando
    tu clase ListaPasajerosPython:
        añadir 3 pasajeros -> listar -> buscar por cédula -> modificar
        -> eliminar -> listar otra vez -> ordenar por NOMBRE con
        sort(key=lambda p: p.nombre)  (es el reto del taller).
    Importa así:  from lista_python import ListaPasajerosPython
                  from pasajero import Pasajero
    """
    from lista_python import ListaPasajerosPython
    from pasajero import Pasajero

    lista = ListaPasajerosPython()
    lista.añadir(Pasajero("Diana", "0923456789", 22))
    lista.añadir(Pasajero("Ana", "0912345678", 28))
    lista.añadir(Pasajero("Luis", "0987654321", 35))
    print("--- Pasajeros añadidos ---")
    lista.listar()

    pos = lista.buscar("0912345678")
    if pos == -1:
        print("No existe")
    else:
        print(f"Encontrado en [{pos}]: {lista.pasajeros[pos]}")

    if lista.modificar("0987654321", "Carlos", 36):
        print("✓ Pasajero modificado")
    if lista.eliminar_por_valor("0912345678"):
        print("✓ Pasajero eliminado")
    print("--- Después de modificar y eliminar ---")
    lista.listar()

    lista.pasajeros.sort(key=lambda p: p.nombre)
    print("--- Ordenados por nombre ---")
    lista.listar()


if __name__ == "__main__":
    ejercicio_t1()
