# Importamos librerías necesarias
import random   # Para elegir caracteres aleatorios
import string   # Para usar letras, números y símbolos predefinidos

# --- Función para generar una contraseña segura ---
def generar_contraseña(longitud=12):
    # Se combinan letras minúsculas y mayúsculas
    # string.ascii_letters = abc...xyzABC...XYZ
    # string.digits = 0123456789
    # "!@#$%&*" = símbolos adicionales
    caracteres = string.ascii_letters + string.digits + "!@#$%&*"

    # "".join() une los caracteres seleccionados
    # random.choice(caracteres) elige un carácter aleatorio de la lista
    # for _ in range(longitud) repite la selección 'longitud' veces
    return "".join(random.choice(caracteres) for _ in range(longitud))

# --- Función que evalúa la fortaleza de una contraseña ---
def evaluar_fortaleza(contraseña):
    comentarios = []   # Aquí guardamos mensajes ✔ o ✘ sobre la contraseña
    puntos = 0         # Contador de seguridad

    # --- Evaluamos la longitud ---
    if len(contraseña) >= 8:           # Si la contraseña tiene 8 o más caracteres
        puntos += 2                    # Sumamos 2 puntos (longitud segura)
        comentarios.append("✔ Longitud adecuada")
    else:                              # Si no cumple
        comentarios.append("✘ Muy corta (mínimo 8 caracteres)")

    # --- Evaluamos mayúsculas ---
    if any(c.isupper() for c in contraseña):   # any() verifica si existe al menos una mayúscula
        puntos += 1                            # Sumamos 1 punto
        comentarios.append("✔ Contiene mayúsculas")
    else:
        comentarios.append("✘ Sin mayúsculas")

    # --- Evaluamos números ---
    if any(c.isdigit() for c in contraseña):   # any() verifica si existe al menos un número
        puntos += 1                            # Sumamos 1 punto
        comentarios.append("✔ Contiene números")
    else:
        comentarios.append("✘ Sin números")

    # --- Evaluación final según puntos acumulados ---
    if puntos >= 4:            # Si tiene 4 puntos o más
        fortaleza = "Muy fuerte"
    elif puntos == 3:          # Si tiene 3 puntos
        fortaleza = "Fuerte"
    elif puntos == 2:          # Si tiene 2 puntos
        fortaleza = "Moderada"
    else:                      # Si tiene 1 o 0 puntos
        fortaleza = "Débil"

    # Retorna la fortaleza y los comentarios
    return fortaleza, comentarios

# --- PROGRAMA PRINCIPAL ---

# Pedimos al usuario que escriba su contraseña
contraseña = input("Ingrese su contraseña:\n")

# Llamamos a la función evaluar_fortaleza con la contraseña ingresada
fortaleza, comentarios = evaluar_fortaleza(contraseña)

# Mostramos un título
print("\nANALIZADOR DE CONTRASEÑAS")
print("=" * 40)   # Imprime 40 signos "=" como separación
print("Resultado:")

# Mostramos la contraseña ingresada por el usuario
print(f"Contraseña: {contraseña}")

# Mostramos la fortaleza calculada (Débil, Moderada, Fuerte o Muy fuerte)
print(f"Fortaleza: {fortaleza}")

# Recorremos la lista de comentarios y mostramos cada uno con " - " adelante
for comentario in comentarios:
    print(f" - {comentario}")

# --- Recomendación si la contraseña no es segura ---
# Si la fortaleza fue Débil o Moderada, sugerimos una nueva contraseña
if fortaleza in ["Débil", "Moderada"]:
    print(f"\n🔑 Recomendación de contraseña segura: {generar_contraseña()}")
