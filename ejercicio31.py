import random  # Importa módulo random para movimientos aleatorios

class Animal:  # Define la clase Animal
    def __init__(self, nombre, tipo, energia=100, posicion_x=0, posicion_y=0):  # Constructor de la clase
        self.nombre = nombre  # Nombre del animal
        self.tipo = tipo  # Tipo de animal: "herbívoro" o "carnívoro"
        self.energia = energia  # Energía inicial
        self.posicion_x = posicion_x  # Posición X inicial
        self.posicion_y = posicion_y  # Posición Y inicial
        self.vivo = True  # Estado de vida inicial

    def mover(self):  # Función para mover el animal
        if self.vivo:  # Solo se mueve si está vivo
            self.posicion_x += random.randint(-1, 1)  # Movimiento aleatorio en X
            self.posicion_y += random.randint(-1, 1)  # Movimiento aleatorio en Y
            self.energia -= 5  # Cada movimiento resta 5 de energía
            if self.energia <= 0:  # Si la energía llega a 0 o menos
                self.vivo = False  # El animal muere
            # Mostrar estado después de moverse
            print(f"{self.nombre} ({self.tipo}) está en ({self.posicion_x}, {self.posicion_y}) con energía {self.energia}, vivo: {self.vivo}")  # Print del estado actual

# === Uso en terminal ===
if __name__ == "__main__":  # Solo ejecuta si es script principal
    leon = Animal("León", "carnívoro")  # Crear León
    conejo = Animal("Conejo", "herbívoro", energia=50)  # Crear Conejo con menos energía

    for turno in range(5):  # Simular 5 turnos
        print(f"\n--- Turno {turno + 1} ---")  # Mostrar número de turno
        leon.mover()  # Mover León
        conejo.mover()  # Mover Conejo
