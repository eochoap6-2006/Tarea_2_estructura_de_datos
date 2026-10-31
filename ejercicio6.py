def ejercicio_p3():
    """
    P3 — Números únicos manteniendo el orden
    Datos: [1, 3, 2, 3, 4, 1, 5, 2]
    ✋ MANUAL : recorrer y añadir si "not in unicos".
    🐍 PYTHON : list(dict.fromkeys(nums))   (y explica por qué list(set(nums))
               NO garantiza el orden)
    Salida esperada: [1, 3, 2, 4, 5]
    """
    nums = [1, 3, 2, 3, 4, 1, 5, 2]
    unicos = []
    for numero in nums:
        if numero not in unicos:
            unicos.append(numero)
    print("MANUAL:", unicos)
    print("PYTHON:", list(dict.fromkeys(nums)))
    print("dict.fromkeys conserva el orden de la primera aparición.")
    print("list(set(nums)) no garantiza ese orden porque un conjunto no conserva el orden de inserción.")


if __name__ == "__main__":
    ejercicio_p3()
