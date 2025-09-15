def pares_con_suma(nums, objetivo):
    vistos = {}  # diccionario para guardar números vistos y sus índices
    pares = []  # lista para almacenar pares encontrados
    for i, n in enumerate(nums):
        complemento = objetivo - n  # número que necesitamos encontrar
        if complemento in vistos:
            pares.append((complemento, n))  # añadimos el par (complemento, n)
        vistos[n] = i  # marcamos el número como visto
    return pares

# Ejemplo
nums = [2,7,11,15,3,6]
print("Pares que suman 9:", pares_con_suma(nums, 9))
