import time  # para medir tiempos

def tiempo_ejecucion(fn):
    # wrapper que envolverá la función original
    def wrapper(*args, **kwargs):
        inicio = time.time()  # tiempo antes de ejecutar
        resultado = fn(*args, **kwargs)  # ejecutamos la función original
        fin = time.time()  # tiempo después de ejecutar
        print(f"Tiempo de ejecución de {fn.__name__}: {fin - inicio:.6f} segundos")  # mostramos tiempo
        return resultado  # devolvemos el resultado original
    return wrapper  # devolvemos el wrapper como nuevo callable

@tiempo_ejecucion
def suma_grande(n):
    # función de ejemplo cuyo tiempo queremos medir
    s = 0
    for i in range(n):
        s += i
    return s

# Ejemplo de uso
print("Suma resultado:", suma_grande(100000))
