def ejercicio_p5():
    """
    P5 — Fusionar dos listas ordenadas (sin sort)
    Datos: a = [1, 3, 5, 7],  b = [2, 4, 6, 8, 10]
    ✋ MANUAL : dos índices i, j comparando cabezas (base del merge sort)
               y al final extend con lo que sobre.
    🐍 PYTHON (para comprobar): sorted(a + b)
    Salida esperada: [1, 2, 3, 4, 5, 6, 7, 8, 10]
    """
    print('P5 — Fusionar dos listas ordenadas (sin sort)')
    a = [1, 3, 5, 7]
    b = [2, 4, 6, 8, 10]
    fusion = []
    i = 0
    j = 0
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            fusion.append(a[i])
            i = i + 1
        else:
            fusion.append(b[j])
            j = j + 1
    fusion.extend(a[i:])
    fusion.extend(b[j:])
    print("MANUAL:", fusion)
    print("PYTHON:", sorted(a + b))


if __name__ == "__main__":
    ejercicio_p5()
