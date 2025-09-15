def busqueda_binaria(lista, elemento_buscado):
    """
    Implementa búsqueda binaria para encontrar un elemento
    La lista debe estar ordenada previamente
    """
    izquierda = 0  # Límite inferior de búsqueda (posición inicial)
    derecha = len(lista) - 1  # Límite superior de búsqueda (última posición de la lista)
    iteraciones = 0  # Contador de iteraciones realizadas

    print(f"Buscando {elemento_buscado} en: {lista}")  # Mostrar qué número se está buscando y en qué lista
    print("\nProceso de búsqueda:")  # Encabezado del proceso

    # Mientras el rango de búsqueda sea válido
    while izquierda <= derecha:
        iteraciones += 1  # Aumentar contador de iteraciones
        medio = (izquierda + derecha) // 2  # Calcular posición central (división entera)
        elemento_medio = lista[medio]  # Obtener el valor en la posición central

        # Mostrar información de la iteración
        print(f"\nIteración {iteraciones}:")
        print(f" Rango: posiciones {izquierda} a {derecha}")  # Rango actual
        print(f" Medio: posición {medio}, valor {elemento_medio}")  # Valor en el medio

        # Comparar el valor medio con el buscado
        if elemento_medio == elemento_buscado:
            print(f" ✔ ¡Encontrado! {elemento_buscado} está en posición {medio}")  # Mensaje de éxito
            return medio  # Retorna la posición encontrada
        elif elemento_medio < elemento_buscado:
            print(f" {elemento_medio} < {elemento_buscado}, buscar en mitad derecha")  # El buscado es mayor
            izquierda = medio + 1  # Mover el límite inferior
        else:
            print(f" {elemento_medio} > {elemento_buscado}, buscar en mitad izquierda")  # El buscado es menor
            derecha = medio - 1  # Mover el límite superior

    # Si salió del bucle, no encontró el número
    print(f"\n{elemento_buscado} no está en la lista")
    print(f"Total de iteraciones: {iteraciones}")  # Mostrar cuántas iteraciones se hicieron
    return -1  # Retornar -1 como no encontrado


def busqueda_lineal(lista, elemento_buscado):
    """Búsqueda lineal para comparar eficiencia"""
    comparaciones = 0  # Contador de comparaciones
    for i in range(len(lista)):  # Recorrer la lista posición por posición
        comparaciones += 1  # Contar la comparación
        if lista[i] == elemento_buscado:  # Si el número coincide
            return i, comparaciones  # Retorna la posición y el número de comparaciones
    return -1, comparaciones  # Si no lo encuentra, devuelve -1 y total de comparaciones


# Lista ordenada de ejemplo
numeros_ordenados = [11, 22, 25, 34, 44, 55, 66, 77, 88, 99]  # Lista ordenada necesaria para la búsqueda binaria

# Pedir al usuario el número que desea buscar
buscar = int(input("Ingrese el número que desea buscar en la lista: "))  # Convierte la entrada a entero

# Encabezado general
print("COMPARACIÓN DE ALGORITMOS DE BÚSQUEDA")
print("=" * 45)
print("Lista ordenada:", numeros_ordenados)  # Mostrar la lista usada
print(f"Elemento a buscar: {buscar}")  # Mostrar el número que se va a buscar

# Búsqueda binaria
print("\n1. BÚSQUEDA BINARIA:")
print("-" * 25)
posicion_binaria = busqueda_binaria(numeros_ordenados, buscar)  # Llamar a la función

# Búsqueda lineal
print("\n2. BÚSQUEDA LINEAL:")
print("-" * 25)
posicion_lineal, comparaciones_lineales = busqueda_lineal(numeros_ordenados, buscar)  # Llamar a la función
print(f"Búsqueda lineal: {comparaciones_lineales} comparaciones")  # Mostrar cuántas comparaciones hizo
if posicion_lineal != -1:  # Si se encontró el número
    print(f"Elemento encontrado en posición {posicion_lineal}")  # Mostrar la posición

# Comparación final de eficiencia
print(f"\nVentaja de búsqueda binaria: Menos comparaciones en listas grandes")
