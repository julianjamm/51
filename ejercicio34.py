import random  # Para generar números aleatorios
import math  # Para cálculos de distancia
from itertools import permutations  # Para crear permutaciones

# Función que calcula la distancia entre dos puntos
def distancia_ciudades(punto1, punto2):
    """Devuelve la distancia euclidiana entre dos ciudades"""
    x_a, y_a = punto1  # Coordenadas primera ciudad
    x_b, y_b = punto2  # Coordenadas segunda ciudad
    resultado = math.sqrt((x_b - x_a)**2 + (y_b - y_a)**2)  # Fórmula
    return round(resultado, 2)  # Redondear a 2 decimales

# Función que calcula distancia total de una ruta
def total_ruta(ciudades, ruta):
    """Suma todas las distancias de la ruta completa"""
    suma = 0  # Acumulador
    for i in range(len(ruta)):  # Iterar sobre ruta
        ciudad_actual = ciudades[ruta[i]]  # Ciudad actual
        siguiente_ciudad = ciudades[ruta[(i + 1) % len(ruta)]]  # Siguiente ciudad (cierra ciclo)
        suma += distancia_ciudades(ciudad_actual, siguiente_ciudad)  # Sumar distancia
    return round(suma, 2)  # Retornar total redondeado

# Método de fuerza bruta para encontrar la ruta más corta
def fuerza_bruta(ciudades):
    """Busca la ruta más corta probando todas las permutaciones"""
    n = len(ciudades)  # Número de ciudades
    print(f"\nAnalizando {n} ciudades para encontrar la ruta más corta...\n")
    mejor = float('inf')  # Mejor distancia inicial
    ruta_optima = None  # Mejor ruta
    for ruta in permutations(range(n)):  # Iterar todas las rutas posibles
        distancia = total_ruta(ciudades, ruta)  # Calcular distancia total
        if distancia < mejor:  # Si es mejor que la anterior
            mejor = distancia  # Actualizar mejor distancia
            ruta_optima = ruta  # Guardar ruta
    return ruta_optima, mejor  # Devolver resultados

# === BLOQUE PRINCIPAL ===
if __name__ == "__main__":
    num_ciudades = int(input("¿Cuántas ciudades desea ingresar? "))  # Input número de ciudades
    ciudades = []  # Lista para almacenar coordenadas
    for i in range(num_ciudades):  # Iterar ciudades
        x = float(input(f"Ingrese coordenada X de la ciudad {i+1}: "))  # Coordenada X
        y = float(input(f"Ingrese coordenada Y de la ciudad {i+1}: "))  # Coordenada Y
        ciudades.append((x, y))  # Guardar tupla (x,y)
    # Calcular mejor ruta
    ruta, distancia_total = fuerza_bruta(ciudades)  # Ejecutar algoritmo
    print("\nResultado de la ruta óptima:")  # Mostrar encabezado
    print(" -> ".join(f"Ciudad {i+1}" for i in ruta))  # Mostrar ruta en orden
    print(f"Distancia total de la ruta: {distancia_total}\n")  # Mostrar distancia total
