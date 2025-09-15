from collections import Counter  # Importa Counter para contar elementos de forma eficiente

def contar_frecuencias(seq):  # Función para contar frecuencia de cada elemento en una secuencia
    if not seq:  # Verifica si la secuencia está vacía
        print("La secuencia está vacía, no hay frecuencias para contar.")  # Mensaje de error
        return Counter()  # Devuelve un Counter vacío
    frec = Counter(seq)  # Crea un diccionario tipo Counter con las frecuencias
    print(f"\nAnalizando secuencia: {seq}")  # Muestra la secuencia que se analiza
    print("Conteo:")  # Encabezado
    for elemento, cantidad in frec.items():  # Recorre cada elemento y su cantidad
        print(f" {elemento}: {cantidad} vez/veces")  # Muestra conteo individual
    return frec  # Retorna el Counter con frecuencias

def mostrar_estadisticas(frec):  # Función para mostrar estadísticas de un conteo
    print("\n" + "=" * 40)  # Línea separadora superior
    print("ESTADÍSTICAS DE FRECUENCIA")  # Título
    print("=" * 40)  # Línea separadora inferior
    orden = frec.most_common()  # Ordena de mayor a menor frecuencia
    total = sum(frec.values())  # Total de elementos contados
    uniq = len(frec)  # Número de elementos únicos
    print(f"Total de elementos: {total}")  # Muestra total
    print(f"Elementos únicos: {uniq}")  # Muestra cantidad de distintos
    print("\nFrecuencias (ordenadas por cantidad):")  # Encabezado
    for elemento, cnt in orden:  # Recorre la lista ordenada
        pct = (cnt / total) * 100 if total else 0  # Calcula porcentaje de cada elemento
        barra = "*" * cnt  # Dibuja una barra visual
        print(f" {str(elemento):>3}: {cnt:>2} veces ({pct:4.1f}%) {barra}")  # Imprime estadística
    mas, mfreq = (orden[0] if orden else (None, 0))  # Identifica el más frecuente
    print(f"\nElemento más frecuente: {mas} ({mfreq} veces)")  # Muestra el más repetido

# -------------------- PROGRAMA PRINCIPAL --------------------
print("CONTADOR DE FRECUENCIAS")
print("=" * 30)

# Ejemplo 1: lista fija de números
numeros = [1, 2, 3, 2, 1, 4, 2, 5, 2, 1, 3, 2]  # Lista predefinida de números
print("\nEJEMPLO CON NÚMEROS:", numeros)  # Muestra lista fija
frecuencias_num = contar_frecuencias(numeros)  # Llama a la función con la lista fija
mostrar_estadisticas(frecuencias_num)  # Muestra estadísticas de esa lista

# Ejemplo 2: lista fija de letras (a partir de un texto)
texto = "programacion"  # Texto fijo de ejemplo
letras = list(texto)  # Convierte el texto en lista de caracteres
print("\nEJEMPLO CON TEXTO:", texto)  # Muestra texto fijo
frecuencias_letras = contar_frecuencias(letras)  # Llama con letras
mostrar_estadisticas(frecuencias_letras)  # Muestra estadísticas

# Ejemplo 3: entrada del usuario
entrada = input("\nIngrese un texto para analizar sus caracteres:\n> ")  # Pide texto al usuario
entrada_lista = list(entrada)  # Convierte la entrada en lista de caracteres
print("\nANÁLISIS DEL TEXTO INGRESADO")  # Encabezado
frecuencias_usuario = contar_frecuencias(entrada_lista)  # Cuenta frecuencias en la entrada
mostrar_estadisticas(frecuencias_usuario)  # Muestra estadísticas de lo ingresado
