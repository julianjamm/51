class Contacto:
    # Constructor con nombre y teléfono
    def __init__(self, nombre, telefono):
        self.nombre = nombre  # guardamos el nombre
        self.telefono = telefono  # guardamos el teléfono

class Agenda:
    # Inicializamos la agenda con una lista vacía
    def __init__(self):
        self.lista = []  # lista donde guardamos objetos Contacto

    def agregar(self, contacto):
        # Agregamos un contacto a la lista
        self.lista.append(contacto)

    def buscar_por_nombre(self, nombre):
        # Buscamos coincidencias (contiene) e ignoramos mayúsculas
        nombre_lower = nombre.lower()
        return [c for c in self.lista if nombre_lower in c.nombre.lower()]

# Ejemplo de uso
a = Agenda()  # creamos una agenda
a.agregar(Contacto("Ana Perez", "300111222"))  # añadimos contacto
a.agregar(Contacto("Andres Gomez", "300333444"))
# Buscamos por 'an' y mostramos teléfonos
result = a.buscar_por_nombre("an")
for r in result:
    print(r.nombre, "-", r.telefono)
