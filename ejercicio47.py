def palabras_comunes_por_linea(texto):
    # Dividimos el texto en líneas
    lineas = [l.strip() for l in texto.splitlines() if l.strip()]
    # Convertimos cada línea en un conjunto de palabras (minúsculas)
    conjuntos = [set(l.lower().split()) for l in lineas]
    if not conjuntos:
        return set()  # si no hay líneas, devolvemos conjunto vacío
    # Intersección de todos los conjuntos para obtener palabras comunes
    comun = conjuntos[0]
    for s in conjuntos[1:]:
        comun = comun.intersection(s)
    return comun

# Ejemplo
texto = "hola mundo\nHola a todos en el mundo\nun mundo para todos"
print("Palabras comunes:", palabras_comunes_por_linea(texto))
