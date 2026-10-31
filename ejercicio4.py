def ejercicio_p1():
    """
    P1 — Contar apariciones de un valor
    Datos: lista = [1, 3, 2, 3, 4, 3, 5],  v = 3
    ✋ MANUAL : patrón contador.   🐍 PYTHON : lista.count(v)
    🧩 COMPRENSIÓN: len([x for x in lista if x == v])
    Salida esperada: 3 aparece 3 veces
    """
    lista = [1, 3, 2, 3, 4, 3, 5]
    v = 3
    contador = 0
    for x in lista:
        if x == v:
            contador = contador + 1
    print(f"MANUAL: {v} aparece {contador} veces")
    print(f"PYTHON: {v} aparece {lista.count(v)} veces")
    contador = len([x for x in lista if x == v])
    print(f"COMPRENSIÓN: {v} aparece {contador} veces")


if __name__ == "__main__":
    ejercicio_p1()
