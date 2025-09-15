def ordenamiento_burbuja(lista):
    """
    Implementa el algoritmo de ordenamiento burbuja
    Compara elementos adyacentes y los intercambia si es necesario
    """
    n = len(lista)  # Tamaño de la lista
    lista_copia = lista.copy()  # Trabajamos con una copia
    comparaciones = 0  # Contador de comparaciones
    intercambios = 0  # Contador de intercambios

    print(f"Lista original: {lista_copia}")
    print("\nProceso paso a paso:")
    # Bucle externo: número de pasadas
    for i in range(n):
        print(f"\n--- Pasada {i + 1} ---")
        hubo_intercambio = False  # Bandera para detectar si hubo cambios
        # Bucle interno: comparaciones en esta pasada
        for j in range(0, n - i - 1):
            comparaciones += 1
            print(f"Comparando {lista_copia[j]} y {lista_copia[j + 1]}")
            # Si el elemento actual es mayor que el siguiente, intercambiar
            if lista_copia[j] > lista_copia[j + 1]:
                lista_copia[j], lista_copia[j + 1] = lista_copia[j + 1], lista_copia[j]
                intercambios += 1
                hubo_intercambio = True
                print(f"\nIntercambio realizado: {lista_copia}")
            else:
                print("\nNo hay intercambio")

        print(f"Estado después de pasada {i + 1}: {lista_copia}")
        # Optimización: si no hubo intercambios, la lista ya está ordenada
        if not hubo_intercambio:
            print("¡No hubo intercambios! La lista ya está ordenada.")
            break

    print(f"\nResultado final: {lista_copia}")
    print("Estadísticas:")
    print(f" - Total de comparaciones: {comparaciones}")
    print(f" - Total de intercambios: {intercambios}")
    return lista_copia


# ---------------- PROBANDO EL ORDENAMIENTO ----------------
print("ALGORITMO DE ORDENAMIENTO BURBUJA")
print("=" * 45)

# Pedir al usuario los números separados por comas
entrada = input("Ingrese los números separados por comas:\n> ")

# Convertimos la entrada en una lista de enteros
numeros = [int(x) for x in entrada.split(",")]

# Ejecutamos el algoritmo
resultado = ordenamiento_burbuja(numeros)
