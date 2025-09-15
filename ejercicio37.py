def comprimir_rangos(nums):
    # Si la lista está vacía devolvemos cadena vacía
    if not nums:  # chequeo rápido de borde
        return ""
    nums = sorted(set(nums))  # ordenamos y removemos duplicados
    # preparamos variables: inicio y fin del rango y lista de resultados
    inicio = nums[0]  # primer elemento inicia el primer rango
    fin = nums[0]  # fin inicia igual que inicio
    partes = []  # lista donde guardaremos los rangos como cadenas
    for n in nums[1:]:  # iteramos desde el segundo elemento
        if n == fin + 1:  # si el siguiente es consecutivo
            fin = n  # extendemos el rango
        else:
            # cerramos el rango actual y lo añadimos a la lista de partes
            if inicio == fin:
                partes.append(str(inicio))  # rango de un solo número
            else:
                partes.append(f"{inicio}-{fin}")  # rango con guion
            inicio = fin = n  # iniciamos nuevo rango con el número actual
    # añadimos el último rango después del bucle
    if inicio == fin:
        partes.append(str(inicio))
    else:
        partes.append(f"{inicio}-{fin}")
    return ",".join(partes)  # unimos las partes con comas

# Ejemplo de uso
nums = [3,2,4,5,10,11,13]
print("Entrada:", nums)
print("Rangos comprimidos:", comprimir_rangos(nums))
