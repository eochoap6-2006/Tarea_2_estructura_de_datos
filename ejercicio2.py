def ejercicio_t2():
    """
    T2 — Estadísticas de una lista de notas   (Taller, Medio)
    -----------------------------------------------------------------
    Datos:  nombres = ["Ana", "Luis", "Diana", "Beto", "Elena"]
            notas   = [ 8,     6,      10,      7,      5  ]
    Muestra: promedio, máxima, mínima, cantidad de aprobados (>= 7)
             y el nombre del mejor estudiante.
    ✋ MANUAL : un solo for con acumulador, campeón y contador.
    🐍 PYTHON : sum, max, min, len, notas.index(max(notas)) y
               aprobados con COMPRENSIÓN: [n for n in notas if n >= 7]
    Salida esperada: Promedio 7.20 · Máx 10 (Diana) · Mín 5 · Aprobados 3 de 5
    """
    print('T2 — Estadísticas de una lista de notas')
    nombres = ["Ana", "Luis", "Diana", "Beto", "Elena"]
    notas = [8, 6, 10, 7, 5]

    total = 0
    maxima = notas[0]
    minima = notas[0]
    mejor = nombres[0]
    aprobados = 0
    cantidad = 0
    for i in range(len(notas)):
        nota = notas[i]
        total = total + nota
        cantidad = cantidad + 1
        if nota > maxima:
            maxima = nota
            mejor = nombres[i]
        if nota < minima:
            minima = nota
        if nota >= 7:
            aprobados = aprobados + 1
    promedio = total / cantidad
    print(f"MANUAL: Promedio {promedio:.2f} · Máx {maxima} ({mejor}) · Mín {minima} · Aprobados {aprobados} de {cantidad}")

    promedio = sum(notas) / len(notas)
    maxima = max(notas)
    minima = min(notas)
    mejor = nombres[notas.index(max(notas))]
    aprobados = [n for n in notas if n >= 7]
    print(f"PYTHON: Promedio {promedio:.2f} · Máx {maxima} ({mejor}) · Mín {minima} · Aprobados {len(aprobados)} de {len(notas)}")


if __name__ == "__main__":
    ejercicio_t2()
