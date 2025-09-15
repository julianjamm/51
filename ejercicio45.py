def roman_to_int(s):
    # Mapa de valores romanos básicos
    vals = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
    total = 0  # acumulador del resultado
    i = 0  # índice para recorrer la cadena
    while i < len(s):
        # Si el siguiente carácter forma par restador (por ejemplo IV = 4)
        if i + 1 < len(s) and vals[s[i]] < vals[s[i+1]]:
            total += vals[s[i+1]] - vals[s[i]]  # sumar la diferencia
            i += 2  # avanzamos dos posiciones
        else:
            total += vals[s[i]]  # sumamos valor simple
            i += 1  # avanzamos una posición
    return total

# Ejemplo
print("MCMLIV =", roman_to_int("MCMLIV"))  # 1954
print("MCMXC =", roman_to_int("MCMXC"))    # 1990
