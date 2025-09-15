def criba(n):
    # Marcamos de 0 a n como True (posible primo) inicialmente
    if n < 2:
        return []
    marcado = [True] * (n + 1)
    marcado[0] = marcado[1] = False  # 0 y 1 no son primos
    p = 2  # empezamos por el primer primo
    while p * p <= n:
        if marcado[p]:
            # marcamos múltiplos de p como no primos
            for multiple in range(p*p, n+1, p):
                marcado[multiple] = False
        p += 1
    # construimos lista de primos a partir del marcado
    return [i for i, is_prime in enumerate(marcado) if is_prime]

# Ejemplo
print("Primos <= 30:", criba(30))
