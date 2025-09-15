nombres = ["Carlos", "Ana", "Pedro", "Lucía", "María", "Jorge", "Sofía"]  # lista inicial de nombres
print("Lista original:", nombres)  # muestra la lista original
print("Cantidad de elementos:", len(nombres))  # len() cuenta cuántos elementos tiene la lista
nombres_ascendente = nombres.copy()  # .copy() crea una copia independiente
nombres_descendente = nombres.copy()  # otra copia para orden descendente
nombres_ascendente.sort()  # .sort() ordena alfabéticamente (A-Z)
print("\nOrdenada ascendente:", nombres_ascendente)
nombres_descendente.sort(reverse=True)  # .sort(reverse=True) ordena de Z-A
print("Ordenada descendente:", nombres_descendente)
import random  # importamos la librería random
nombres_mezclados = nombres.copy()  # .copy() otra copia para mezclar
random.shuffle(nombres_mezclados)  # .shuffle() mezcla los nombres en orden aleatorio
print("Lista mezclada:", nombres_mezclados)
nombres_invertidos = nombres.copy()  # .copy() para no alterar la original
nombres_invertidos.reverse()  # .reverse() invierte el orden actual
print("Orden invertido:", nombres_invertidos)
print("\nLista original (sin cambios):", nombres)  # muestra que la lista original sigue intacta
