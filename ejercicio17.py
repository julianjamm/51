# Lista de animales inteligente
animales = ["perro", "gato", "conejo"]
print("Lista inicial:\n", animales)
# Agregar elementos al final
animales.append("loro")
animales.append("pez")
print("Después de agregar loro y pez:\n", animales)
# Insertar en posición específica
animales.insert(1, "hamster")
print("Después de insertar hamster en posición 1:\n", animales)
# Eliminar elementos por valor
animales.remove("conejo")
print("Después de eliminar conejo:\n", animales)
# Eliminar por posición
eliminado = animales.pop(0)
print("Eliminamos el primer animal:", eliminado,"\n Lista final:", animales)