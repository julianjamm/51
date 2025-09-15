import random  # Para generar aleatoriedad en el tablero
import time  # Para pausas entre generaciones

# Función para crear el tablero inicial
def generar_tablero(filas, columnas, prob_viva=0.3):
    """Crea un tablero con células vivas (1) y muertas (0)"""
    tablero = []  # Lista que contendrá el tablero completo
    for i in range(filas):  # Iterar sobre filas
        fila_actual = []  # Lista para la fila actual
        for j in range(columnas):  # Iterar sobre columnas
            # Asignar 1 (viva) o 0 (muerta) según probabilidad
            estado = 1 if random.random() < prob_viva else 0
            fila_actual.append(estado)  # Agregar célula a la fila
        tablero.append(fila_actual)  # Agregar fila al tablero
    return tablero  # Devolver tablero completo

# Función para contar vecinos vivos de una célula
def contar_vecinos(tablero, fila, columna):
    """Cuenta los 8 vecinos vivos de una célula"""
    filas = len(tablero)  # Número de filas
    columnas = len(tablero[0])  # Número de columnas
    total_vivos = 0  # Contador de vecinos vivos
    # Todas las posiciones relativas de los 8 vecinos
    direcciones = [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]
    for df, dc in direcciones:  # Iterar sobre cada dirección
        nueva_fila = fila + df  # Calcular fila del vecino
        nueva_col = columna + dc  # Calcular columna del vecino
        # Verificar que esté dentro del tablero
        if 0 <= nueva_fila < filas and 0 <= nueva_col < columnas:
            total_vivos += tablero[nueva_fila][nueva_col]  # Sumar si el vecino está vivo
    return total_vivos  # Devolver cantidad de vecinos vivos

# Función que aplica las reglas del Juego de la Vida
def siguiente_generacion(tablero):
    """Genera la próxima generación según las reglas"""
    filas = len(tablero)  # Número de filas
    columnas = len(tablero[0])  # Número de columnas
    nuevo_tablero = [[0 for _ in range(columnas)] for _ in range(filas)]  # Crear nuevo tablero vacío
    cambios = []  # Lista para registrar cambios de estado

    for i in range(filas):  # Iterar filas
        for j in range(columnas):  # Iterar columnas
            vecinos = contar_vecinos(tablero, i, j)  # Contar vecinos vivos
            celula = tablero[i][j]  # Estado actual de la célula
            nueva_celula = celula  # Por defecto mantiene el estado

            if celula == 1:  # Célula viva
                if vecinos < 2:  # Soledad
                    nueva_celula = 0
                    cambios.append((i, j, "murió por soledad"))
                elif vecinos > 3:  # Sobrepoblación
                    nueva_celula = 0
                    cambios.append((i, j, "murió por sobrepoblación"))
                # Si tiene 2 o 3 vecinos, sobrevive (no se registra cambio)
            else:  # Célula muerta
                if vecinos == 3:  # Nace nueva célula
                    nueva_celula = 1
                    cambios.append((i, j, "nació"))
            nuevo_tablero[i][j] = nueva_celula  # Asignar al nuevo tablero
    return nuevo_tablero, cambios  # Devolver nuevo tablero y lista de cambios

# Función para mostrar el tablero en pantalla
def imprimir_tablero(tablero, generacion):
    """Imprime el tablero de forma visual en terminal"""
    print(f"\nGeneración {generacion}:")  # Encabezado con número de generación
    for fila in tablero:  # Iterar sobre filas
        linea = ""  # String para formar la fila
        for celula in fila:  # Iterar sobre células
            linea += "█" if celula == 1 else " "  # █ = viva, espacio = muerta
        print(linea)  # Imprimir la fila
    print("-" * len(tablero[0]))  # Línea separadora

# Función principal del autómata
def simular_juego_de_la_vida(filas, columnas, generaciones=10, densidad=0.3, delay=0.5):
    """Simula el autómata celular completo"""
    tablero = generar_tablero(filas, columnas, densidad)  # Crear tablero inicial
    for gen in range(1, generaciones + 1):  # Iterar generaciones
        imprimir_tablero(tablero, gen)  # Mostrar tablero
        tablero, cambios = siguiente_generacion(tablero)  # Calcular siguiente generación
        time.sleep(delay)  # Pausa entre generaciones
        # Mostrar cambios si se desea
        if cambios:
            for cambio in cambios:
                i, j, descripcion = cambio
                print(f"Célula ({i},{j}): {descripcion}")

# === EJEMPLO DE USO ===
if __name__ == "__main__":
    filas_usuario = int(input("Número de filas: "))  # Input filas
    columnas_usuario = int(input("Número de columnas: "))  # Input columnas
    generaciones_usuario = int(input("Número de generaciones: "))  # Input generaciones
    simular_juego_de_la_vida(filas_usuario, columnas_usuario, generaciones_usuario)  # Ejecutar simulación
