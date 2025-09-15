import random  # para decisiones aleatorias y mecánicas simples

def mostrar_intro():
    # Presentación breve del juego
    print("=== AVENTURA: La Fortaleza ===")
    print("Tu objetivo: llegar a la sala del tesoro evitando trampas y llegando con al menos 3 llaves.")
    print("En cada etapa puedes elegir una acción. Usa números para seleccionar opciones.")

def elegir_ruta():
    # El jugador elige entre dos rutas: segura o arriesgada
    print("\nElige una ruta:")
    print("1) Ruta segura (menos eventos, pero menos recompensas)")
    print("2) Ruta arriesgada (más eventos, más recompensas)")
    while True:
        opt = input("Tu elección (1/2): ").strip()
        if opt in ('1','2'):
            return opt
        print("Entrada no válida, intenta de nuevo.")

def evento(ruta, estado):
    # Genera un evento según ruta: devuelve cambios en estado
    # Estado es un diccionario con llaves: 'vidas', 'llaves', 'oro'
    if ruta == '1':
        # Ruta segura: mayor probabilidad de encontrar oro o nada
        roll = random.random()
        if roll < 0.1:
            print("Encontraste una trampa leve! Pierdes 1 vida.")
            estado['vidas'] -= 1
        elif roll < 0.5:
            print("Encontraste 1 oro.")
            estado['oro'] += 1
        else:
            print("Camino tranquilo...")
    else:
        # Ruta arriesgada: más probabilidades de llaves o trampas
        roll = random.random()
        if roll < 0.2:
            print("Trampa peligrosa! Pierdes 1 vida.")
            estado['vidas'] -= 1
        elif roll < 0.5:
            print("Encontraste una llave dorada!")
            estado['llaves'] += 1
        else:
            print("Encontraste algo de oro.")
            estado['oro'] += 1
    return estado

def sala_tesoro(estado):
    # Verifica si el jugador puede abrir la sala del tesoro
    print("\nHas llegado a la sala del tesoro...")
    # Condición para abrir la sala: tener >=3 llaves Y al menos 1 vida
    if estado['llaves'] >= 3 and estado['vidas'] > 0:
        print("¡Con tus llaves logras abrir el cofre y ganar el juego!")
        return True
    # Si no tiene llaves suficientes OR no tiene vidas, se producen consecuencias
    if estado['llaves'] < 3 or estado['vidas'] <= 0:
        # Usamos or/not para comprobar situaciones: si no tiene llaves OR no vive, pierde.
        if not (estado['llaves'] >= 3) or estado['vidas'] <= 0:
            print("No puedes abrir el cofre. Te retiran de la fortaleza...")
            return False
    return False

def jugar():
    mostrar_intro()  # mostramos introducción
    # Estado inicial del jugador
    estado = {'vidas': 3, 'llaves': 0, 'oro': 0}
    rondas = 0  # contador de rondas recorridas
    # El bucle principal: el jugador decide avanzar hasta 10 rondas o morir
    while rondas < 10 and estado['vidas'] > 0:
        rondas += 1  # incrementamos rondas
        print(f"\n--- Ronda {rondas} ---")
        ruta = elegir_ruta()  # jugador elige ruta
        # Realizamos de 1 a 3 eventos en la ruta elegida (uso de for)
        eventos = random.randint(1,3)
        for _ in range(eventos):
            estado = evento(ruta, estado)  # aplicamos evento y actualizamos estado
            # Si el jugador pierde todas las vidas salimos del bucle inmediatamente
            if estado['vidas'] <= 0:
                print("Has perdido todas tus vidas!")
                break
        # Decisión adicional: si tienes 2 o más llaves puedes intentar forzar la entrada (riesgoso)
        if estado['llaves'] >= 2:
            print("Tienes varias llaves. ¿Intentar forzar la puerta arriesgando una vida? (s/n)")
            intento = input().strip().lower()
            # Ejemplo de uso de operadores lógicos: si dice 's' y tiene >0 vidas -> riesgo
            if intento == 's' and estado['vidas'] > 0:
                # Riesgo: 50% éxito
                if random.random() < 0.5:
                    print("El intento funcionó! Ganas una llave adicional.")
                    estado['llaves'] += 1
                else:
                    print("Fallaste y perdiste 1 vida.")
                    estado['vidas'] -= 1
        # Mostrar estado actual después de la ronda
        print("Estado actual:", estado)
        # Si el jugador ya tiene 3 o más llaves, preguntar si quiere ir a la sala del tesoro
        if estado['llaves'] >= 3:
            print("¿Deseas intentar abrir la sala del tesoro ahora? (s/n)")
            if input().strip().lower() == 's':
                break  # salimos del bucle principal para ir a la sala
    # Al salir del bucle principal, comprobamos la sala del tesoro
    exito = sala_tesoro(estado)
    if exito:
        print("¡Felicidades, victoria!")
    else:
        print("Fin del juego. Mejor suerte la próxima.")

if __name__ == '__main__':
    jugar()  # iniciamos el juego si ejecutamos el script directamente
