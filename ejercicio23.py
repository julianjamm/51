def contar_palabras(t):
    # t: string con el texto a analizar
    # split() separa el texto en palabras y len() cuenta cuántas hay
    return len(t.split())

def contar_caracteres(t, espacios=True):
    # t: string con el texto a analizar
    # espacios: bool que indica si contamos los espacios (True) o no (False)
    if espacios:
        # len() devuelve el número total de caracteres, incluidos los espacios
        return len(t)
    else:
        # replace(" ", "") elimina los espacios antes de contar los caracteres
        return len(t.replace(" ", ""))

def encontrar_palabra_mas_larga(t):
    # t: string con el texto a analizar
    # split() crea una lista de palabras; max(..., key=len) devuelve la más larga
    # default="" evita error si t está vacío
    return max(t.split(), key=len, default="")

def es_palindromo(t):
    # t: string con el texto a analizar
    # Normalizamos: pasamos a minúsculas y quitamos espacios para comparar correctamente
    t_limpio = t.lower().replace(" ", "")
    # Comparamos el texto limpio con su versión invertida [::-1]
    return t_limpio == t_limpio[::-1]

# Pedimos la frase al usuario (input() siempre devuelve un string)
frase = input("Ingrese una frase:\n")

# Imprimimos los resultados usando las funciones definidas arriba
print("\nANALIZADOR DE TEXTO")
print(f"Texto: '{frase}'")
print("-" * 50)
print(f"Palabras: {contar_palabras(frase)}")
print(f"Caracteres (con espacios): {contar_caracteres(frase)}")
print(f"Caracteres (sin espacios): {contar_caracteres(frase, False)}")
print(f"Palabra más larga: '{encontrar_palabra_mas_larga(frase)}'")
print(f"¿Es palíndromo?: {es_palindromo(frase)}")
