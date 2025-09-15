contraseña = str(input("Escribe tu contraseña con una longitud mínima de 8 caracteres:\n"))# Solicita al usuario que escriba una contraseña
longitud_minima = 8# Define la longitud mínima permitida para la contraseña
print("Contraseña a validar:\n", contraseña)# Muestra la contraseña ingresada
print("Longitud de la contraseña:", len(contraseña))# Muestra cuántos caracteres tiene la contraseña
# Verifica si la contraseña cumple con la longitud mínima
if len(contraseña) >= longitud_minima:
    print("La contraseña tiene la longitud correcta") # Si cumple, muestra mensaje de validación
else:
    print(f"La contraseña no tiene la longitud necesaria, que es de al menos {longitud_minima} caracteres")# Si no cumple, muestra mensaje de error
