# Definimos el número secreto que el jugador debe adivinar
numero_secreto = 7
# Número máximo de intentos permitidos
intentos_maximos = 3
# Contador para el intento actual
intento_actual = 1
print("¡Bienvenido al juego de adivinanza!\nTienes", intentos_maximos, "intentos para adivinar el número del 1 al 10")
# Bucle que se ejecuta mientras no se superen los intentos
while intento_actual <= intentos_maximos:
    print("\n--- Intento", intento_actual, "de", intentos_maximos, "---")
    # El jugador ingresa su adivinanza (convertida a entero)
    adivinanza = int(input("Escribe tu adivinanza: "))
    # Muestra la adivinanza
    print("Tu adivinanza:", adivinanza)
    # Verifica si la adivinanza es correcta
    if adivinanza == numero_secreto:
        print("¡GANASTE! El número era", numero_secreto)
        break  # Salimos del bucle si ganó
    elif adivinanza < numero_secreto:
        print("El número es mayor")
    else:
        print("El número es menor")
    # Aumenta el intento actual
    intento_actual = intento_actual + 1
# Si se usaron todos los intentos y no adivinó
if intento_actual > intentos_maximos:
    print("¡Se acabaron los intentos! El número era", numero_secreto)