def ejercicio_t3():
    """
    T3 — Ordenar una lista (bubble sort)   (Taller, Avanzado)
    -----------------------------------------------------------------
    Datos: [5, 2, 8, 1, 9, 3, 7]
    ✋ MANUAL : burbuja con bandera hubo_swap (sobre una COPIA lista[:]).
    🐍 PYTHON : sorted(lista) y lista.sort(reverse=True).
    Extra    : palabras = ["python", "a", "código", "el"] ordenadas con key=len
    Salida esperada: [1, 2, 3, 5, 7, 8, 9]
    """
    lista = [5, 2, 8, 1, 9, 3, 7]
    copia = lista[:]
    for vuelta in range(len(copia) - 1):
        hubo_swap = False
        for i in range(len(copia) - 1 - vuelta):
            if copia[i] > copia[i + 1]:
                aux = copia[i]
                copia[i] = copia[i + 1]
                copia[i + 1] = aux
                hubo_swap = True
        if not hubo_swap:
            break
    print("MANUAL:", copia)
    print("Original:", lista)
    print("PYTHON ascendente:", sorted(lista))
    lista.sort(reverse=True)
    print("PYTHON descendente:", lista)

    palabras = ["python", "a", "código", "el"]
    palabras.sort(key=len)
    print("Palabras por longitud:", palabras)


if __name__ == "__main__":
    ejercicio_t3()
