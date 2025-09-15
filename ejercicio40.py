def son_anagramas(a, b):
    # Eliminamos espacios y pasamos a minúsculas
    a_clean = "".join(a.split()).lower()
    b_clean = "".join(b.split()).lower()
    # Si longitudes difieren, no pueden ser anagramas
    if len(a_clean) != len(b_clean):
        return False
    # Contamos caracteres usando diccionarios
    conteo = {}
    for ch in a_clean:
        conteo[ch] = conteo.get(ch, 0) + 1
    for ch in b_clean:
        if ch not in conteo or conteo[ch] == 0:
            return False
        conteo[ch] -= 1
    # Si llegamos aquí, son anagramas
    return True

# Ejemplo
print("roma / amor ->", son_anagramas("roma", "amor"))
print("animo / monia ->", son_anagramas("animo", "monia"))
