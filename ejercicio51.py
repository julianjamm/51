import random  # Importamos la librería random para generar decisiones aleatorias

def mostrar_intro():
    # Función que muestra la introducción del juego
    print("=== AVENTURA: La Fortaleza ===\nTu objetivo: llegar a la sala del tesoro evitando trampas y llegando con al menos 3 llaves.")  # Título del juego Explicación del objetivo
    print("En cada etapa puedes elegir una acción. Usa números para seleccionar opciones.")  # Instrucciones de juego

def elegir_ruta():
    # Función que pide al jugador elegir entre dos rutas posibles
    print("\nElige una ruta:")  # Texto de selección
    print("1) Ruta segura (menos eventos, pero menos recompensas)")  # Opción 1
    print("2) Ruta arriesgada (más eventos, más recompensas)")  # Opción 2
    while True:  # Bucle hasta que elija bien
        opt = input("Tu elección (1/2): ").strip()  # Pedimos entrada y eliminamos espacios
        if opt in ('1','2'):  # Validamos que sea '1' o '2'
            return opt  # Devolvemos la elección válida
        print("Entrada no válida, intenta de nuevo.")  # Mensaje de error

def evento(ruta, estado):
    # Función que genera un evento según la ruta elegida
    # El parámetro estado es un diccionario con 'vidas', 'llaves' y 'oro'
    if ruta == '1':  # Si eligió ruta segura
        roll = random.random()  # Generamos un número aleatorio entre 0 y 1
        if roll < 0.1:  # 10% de probabilidad de trampa
            print("Encontraste una trampa leve! Pierdes 1 vida.")
            estado['vidas'] -= 1  # Restamos 1 vida
        elif roll < 0.5:  # 40% de probabilidad de encontrar oro
            print("Encontraste 1 oro.")
            estado['oro'] += 1  # Sumamos 1 oro
        else:  # 50% de probabilidad de nada
            print("Camino tranquilo...")
    else:  # Si eligió ruta arriesgada
        roll = random.random()  # Número aleatorio entre 0 y 1
        if roll < 0.2:  # 20% de trampa peligrosa
            print("Trampa peligrosa! Pierdes 1 vida.")
            estado['vidas'] -= 1
        elif roll < 0.5:  # 30% de probabilidad de llave
            print("Encontraste una llave dorada!")
            estado['llaves'] += 1
        else:  # 50% de probabilidad de oro
            print("Encontraste algo de oro.")
            estado['oro'] += 1
    return estado  # Devolvemos el estado actualizado

def sala_tesoro(estado):
    # Función que evalúa si el jugador puede ganar
    print("\nHas llegado a la sala del tesoro...")  # Mensaje de llegada
    # Condición de victoria: tener al menos 3 llaves y al menos 1 vida
    if estado['llaves'] >= 3 and estado['vidas'] > 0:  # Uso de AND
        print("¡Con tus llaves logras abrir el cofre y ganar el juego!")
        return True
    # Si no cumple, mostramos mensaje de fracaso
    if estado['llaves'] < 3 or estado['vidas'] <= 0:  # Uso de OR
        # Aquí usamos NOT para invertir la condición de victoria
        if not (estado['llaves'] >= 3 and estado['vidas'] > 0):  # Uso de NOT
            print("No puedes abrir el cofre. Te retiran de la fortaleza...")
            return False
    return False  # Si no cumple condiciones, devuelve False

def jugar():
    # Función principal que ejecuta el juego completo
    mostrar_intro()  # Llamamos la introducción
    estado = {'vidas': 3, 'llaves': 0, 'oro': 0}  # Creamos el estado inicial
    rondas = 0  # Contador de rondas

    # Bucle principal: máximo 10 rondas y solo si tiene vidas
    while rondas < 10 and estado['vidas'] > 0:  # Uso de AND
        rondas += 1  # Aumentamos contador de rondas
        print(f"\n--- Ronda {rondas} ---")  # Mostramos número de ronda
        ruta = elegir_ruta()  # El jugador elige la ruta

        # Advertencia si está en peligro (pocas vidas o sin recursos)
        if estado['vidas'] <= 1 or (not estado['llaves'] and not estado['oro']):  # Uso de OR para peligro y dentro uso not y and not para recursos
            print("⚠️ Consejo: Estás en peligro, juega con cuidado.")

        # Generamos de 1 a 3 eventos según la ruta
        for _ in range(random.randint(1, 3)):  # Bucle FOR
            estado = evento(ruta, estado)  # Aplicamos evento
            if estado['vidas'] <= 0:  # Si pierde todas las vidas
                print("Has perdido todas tus vidas!")
                break  # Salimos del for

        # Si tiene al menos 2 llaves puede intentar forzar la puerta
        if estado['llaves'] >= 2 and estado['vidas'] > 0:  # Uso de AND
            print("Tienes varias llaves. ¿Intentar forzar la puerta arriesgando una vida? (s/n)")
            intento = input().strip().lower()  # Pedimos decisión
            if intento == 's' and estado['vidas'] > 0:  # Uso de AND
                if random.random() < 0.5:  # 50% éxito
                    print("El intento funcionó! Ganas una llave adicional.")
                    estado['llaves'] += 1
                else:
                    print("Fallaste y perdiste 1 vida.")
                    estado['vidas'] -= 1

        print("Estado actual:", estado)  # Mostramos estado actual

        # Si ya tiene 3 llaves puede intentar abrir la sala del tesoro
        if estado['llaves'] >= 3 and estado['vidas'] > 0:  # Uso de AND
            print("¿Deseas intentar abrir la sala del tesoro ahora? (s/n)")
            if input().strip().lower() == 's':  # Si responde que sí
                break  # Rompemos el while para ir a la sala

    # Comprobamos si gana o pierde al final
    exito = sala_tesoro(estado)  # Llamamos la función de victoria
    if exito:  # Si devuelve True
        print("¡Felicidades, victoria!")  # Mensaje de victoria
    else:  # Si devuelve False
        print("Fin del juego. Mejor suerte la próxima.")  # Mensaje de derrota

# Punto de entrada principal del programa
if __name__ == '__main__':  # Si ejecutamos directamente este archivo
    jugar()  # Llamamos la función principal
