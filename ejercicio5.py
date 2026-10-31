def ejercicio_p2():
    """
    P2 — Invertir una lista SIN lista.reverse()
    Datos: [1, 2, 3, 4, 5]
    ✋ MANUAL : for con range(len(lista)-1, -1, -1) y append.
    🐍 PYTHON : lista[::-1]  y  list(reversed(lista))
    🧩 COMPRENSIÓN: [lista[i] for i in range(len(lista)-1, -1, -1)]
    Salida esperada: [5, 4, 3, 2, 1]
    """
    print('P2 — Invertir una lista SIN lista.reverse()')
    lista = [1, 2, 3, 4, 5]
    invertida = []
    for i in range(len(lista) - 1, -1, -1):
        invertida.append(lista[i])
    print("MANUAL:", invertida)
    print("PYTHON slicing:", lista[::-1])
    print("PYTHON reversed:", list(reversed(lista)))
    invertida = [lista[i] for i in range(len(lista) - 1, -1, -1)]
    print("COMPRENSIÓN:", invertida)


if __name__ == "__main__":
    ejercicio_p2()
