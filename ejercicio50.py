def lps_array(pat):
    # Construye el array LPS (longest proper prefix which is also suffix)
    n = len(pat)
    lps = [0] * n  # inicializamos con ceros
    length = 0  # longitud del prefijo más largo
    i = 1  # empezamos desde el segundo carácter
    while i < n:
        if pat[i] == pat[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]  # retrocedemos usando LPS
            else:
                lps[i] = 0
                i += 1
    return lps

def kmp_search(text, pat):
    # Buscamos todas las ocurrencias de pat en text usando LPS
    if not pat:
        return []  # patrón vacío -> devolvemos lista vacía de posiciones
    lps = lps_array(pat)  # calculamos LPS del patrón
    res = []  # posiciones donde ocurre el patrón
    i = j = 0  # i para text, j para pattern
    while i < len(text):
        if text[i] == pat[j]:
            i += 1
            j += 1
            if j == len(pat):
                res.append(i - j)  # añadimos posición de inicio
                j = lps[j - 1]  # continuamos búsqueda
        else:
            if j != 0:
                j = lps[j - 1]  # retrocedemos en patrón
            else:
                i += 1  # avanzamos en texto
    return res

# Ejemplo
texto = "ABABDABACDABABCABAB"
pat = "ABABCABAB"
print("Posiciones:", kmp_search(texto, pat))
