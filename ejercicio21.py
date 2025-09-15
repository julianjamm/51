# Definimos una función llamada "saludar" que recibe un parámetro (nombre)
def saludar(nombre):  
    # Esta función construye un mensaje usando el nombre
    mensaje = f"¡Hola {nombre}! ¿Cómo estás?"
    return mensaje  # Devuelve el mensaje creado
# Pedimos al usuario que ingrese varios nombres (separados por comas)
# split(",") divide los nombres en una lista
nombres = input("Escribe varios nombres separados por comas: ").split(",")
# Mostramos un título antes de los saludos
print("Usando mi función de saludo:")
# Recorremos la lista de nombres y saludamos a cada persona
for nombre in nombres:
    print(saludar(nombre.strip()))  # strip() quita espacios extras