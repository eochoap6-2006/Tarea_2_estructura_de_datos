def ejercicio_p4():
    """
    P4 — Segundo mayor (sin ordenar toda la lista)
    Datos: [5, 2, 9, 7, 9, 3, 8]
    ✋ MANUAL : dos campeones (mayor y segundo) en un solo recorrido.
    🐍 PYTHON (para comprobar): sorted(set(nums))[-2]
    Salida esperada: Mayor 9 · Segundo 8
    """
    print('P4 — Segundo mayor (sin ordenar toda la lista)')
    nums = [5, 2, 9, 7, 9, 3, 8]
    mayor = None
    segundo = None
    for numero in nums:
        if mayor is None or numero > mayor:
            segundo = mayor
            mayor = numero
        elif numero != mayor and (segundo is None or numero > segundo):
            segundo = numero
    if segundo is None:
        print("No hay dos valores distintos")
    else:
        print(f"MANUAL: Mayor {mayor} · Segundo {segundo}")
    print(f"PYTHON: Mayor {max(nums)} · Segundo {sorted(set(nums))[-2]}")


if __name__ == "__main__":
    ejercicio_p4()
