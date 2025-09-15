import os

# Usamos una ruta local relativa para que funcione en cualquier PC
ruta = "archivo_ejemplo_38.txt"

# Si el archivo no existe, creamos uno de ejemplo
if not os.path.exists(ruta):
    with open(ruta, "w", encoding="utf-8") as f:
        f.write("Hola mundo\nEsta es una prueba\nUna línea más")  # contenido ejemplo

# Abrimos el archivo y leemos su contenido
with open(ruta, "r", encoding="utf-8") as f:
    contenido = f.read()  # leemos todo el archivo como una sola cadena

# Contamos caracteres totales usando len()
caracteres = len(contenido)  # total de caracteres incluyendo saltos de línea

# Contamos líneas separando por '\n'
lineas = contenido.splitlines()  # lista de líneas sin '\n'
num_lineas = len(lineas)  # número de líneas

# Contamos palabras: rompemos por cualquier espacio y filtramos entradas vacías
palabras = [w for w in contenido.split() if w.strip()]  # lista de palabras
num_palabras = len(palabras)  # número de palabras

# Mostramos resultados
print("Líneas:", num_lineas)
print("Palabras:", num_palabras)
print("Caracteres:", caracteres)
