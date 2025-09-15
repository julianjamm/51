import re  # usamos expresiones regulares para limpiar el texto

texto = "Hola hola! ¿Cómo estás? Hola, bien; bien y tú."  # texto de ejemplo

# Convertimos el texto a minúsculas para tratar 'Hola' y 'hola' como la misma palabra
texto_minus = texto.lower()  # todas las letras en minúscula

# Eliminamos caracteres que no sean letras, números o espacios
texto_limpio = re.sub(r'[^a-z0-9\s]', '', texto_minus)  # quita signos de puntuación

# Dividimos el texto en palabras usando espacios como separador
palabras = texto_limpio.split()  # lista de palabras

# Creamos un diccionario para contar frecuencias
frecuencia = {}  # diccionario vacío donde guardaremos conteos

# Recorremos cada palabra y aumentamos su contador en el diccionario
for p in palabras:  # iteramos por cada palabra en la lista
    frecuencia[p] = frecuencia.get(p, 0) + 1  # sumar 1 al contador (si no existe, get devuelve 0)

# Mostramos el diccionario de frecuencias ordenado por frecuencia descendente
frecuencia_ordenada = dict(sorted(frecuencia.items(), key=lambda x: x[1], reverse=True))  # ordena por valor
print("Frecuencia por palabra:", frecuencia_ordenada)  # impresión final del resultado
