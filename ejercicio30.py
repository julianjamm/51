# Definición de la función que calcula la similitud entre dos usuarios (recibe dos diccionarios)
def calcular_similitud(usuario1, usuario2):  # calcula la fracción de categorías donde coinciden los gustos
    gustos_comunes = 0  # contador de coincidencias en gustos
    total_comparaciones = 0  # contador de categorías comparadas

    for categoria in usuario1:  # recorre cada categoría presente en usuario1
        if categoria in usuario2:  # verifica que la misma categoría exista en usuario2
            total_comparaciones += 1  # incrementa el total de comparaciones realizadas
            if usuario1[categoria] == usuario2[categoria]:  # comprueba si ambos tienen el mismo valor (True/False)
                gustos_comunes += 1  # si coinciden, incrementa el contador de coincidencias

    if total_comparaciones == 0:  # si no hubo categorías comunes para comparar
        return 0  # retorna 0 de similitud al no poder comparar nada

    return round(gustos_comunes / total_comparaciones, 2)  # calcula y retorna la similitud redondeada a 2 decimales


# Definición de la función que encuentra usuarios similares al usuario objetivo dado un umbral
def encontrar_usuarios_similares(usuario_objetivo, base_usuarios, umbral=0.6):  # recibe nombre objetivo, base y umbral
    similares = []  # lista para almacenar tuplas (nombre_usuario, similitud)
    gustos_objetivo = base_usuarios[usuario_objetivo]  # obtiene el diccionario de gustos del usuario objetivo
    print(f"\nBuscando usuarios similares a '{usuario_objetivo}' (umbral: {umbral})")  # informa la búsqueda
    print("-" * 45)  # línea separadora visual

    for nombre_usuario, gustos_usuario in base_usuarios.items():  # recorre la base de usuarios
        if nombre_usuario != usuario_objetivo:  # evita comparar el usuario consigo mismo
            similitud = calcular_similitud(gustos_objetivo, gustos_usuario)  # calcula similitud con cada usuario
            print(f"{nombre_usuario}: {similitud * 100:.0f}% similar")  # muestra porcentaje de similitud
            if similitud >= umbral:  # si la similitud cumple o supera el umbral
                similares.append((nombre_usuario, similitud))  # añade a la lista de similares

    similares.sort(key=lambda x: x[1], reverse=True)  # ordena la lista por similitud de mayor a menor
    return similares  # devuelve la lista ordenada de usuarios similares


# Definición de la función que genera recomendaciones basadas en usuarios similares
def recomendar_contenido(usuario_objetivo, usuarios_similares, base_usuarios):  # recibe objetivo, lista de similares y base
    recomendaciones = {}  # diccionario para acumular recomendaciones: categoria -> lista de (usuario, similitud)
    gustos_objetivo = base_usuarios[usuario_objetivo]  # obtiene gustos del usuario objetivo
    print(f"\nGenerando recomendaciones para '{usuario_objetivo}':")  # informa que inicia la generación de recomendaciones

    for nombre_similar, similitud in usuarios_similares:  # recorre cada usuario similar provisto
        gustos_similar = base_usuarios[nombre_similar]  # obtiene los gustos del usuario similar
        print(f"\nAnalizando gustos de {nombre_similar} (similitud: {similitud})")  # muestra quién se analiza
        for categoria, le_gusta in gustos_similar.items():  # recorre las categorías y si al similar le gusta
            if categoria not in gustos_objetivo and le_gusta:  # si el objetivo no tiene registro de esa categoría y al similar le gusta
                if categoria not in recomendaciones:  # si aún no existe la categoría en recomendaciones
                    recomendaciones[categoria] = []  # inicializa la lista para esa categoría
                recomendaciones[categoria].append((nombre_similar, similitud))  # añade el recomendador y su similitud
                print(f"  Recomendar '{categoria}' (le gusta a {nombre_similar})")  # imprime la acción de recomendación

    return recomendaciones  # retorna el diccionario de recomendaciones


# -----------------------------------------------------
# Base de datos de ejemplo con usuarios y sus preferencias
# -----------------------------------------------------
usuarios = {  # diccionario principal: nombre_usuario -> diccionario de categorías: bool
    "Ana": {"acción": True, "comedia": True, "drama": False, "terror": False, "ciencia_ficción": True},  # gustos de Ana
    "Carlos": {"acción": True, "comedia": False, "drama": True, "terror": False, "ciencia_ficción": True},  # gustos de Carlos
    "María": {"acción": False, "comedia": True, "drama": True, "terror": True, "ciencia_ficción": False},  # gustos de María
    "Pedro": {"acción": True, "comedia": True, "drama": False, "terror": False, "ciencia_ficción": False},  # gustos de Pedro
    "Laura": {"acción": False, "comedia": True, "drama": True, "terror": False, "ciencia_ficción": True}  # gustos de Laura
}  # fin de la estructura de usuarios


# ------------------ PROGRAMA PRINCIPAL INTERACTIVO ------------------
print("SISTEMA DE RECOMENDACIONES")  # título del sistema
print("=" * 40)  # línea separadora visual

print("Usuarios disponibles:")  # imprime encabezado de usuarios disponibles
for usuario in usuarios:  # itera sobre las claves del diccionario de usuarios
    print(f"- {usuario}")  # imprime cada usuario disponible

# Solicita al usuario objetivo mediante input y normaliza la capitalización
usuario_objetivo = input("\nIngrese el nombre del usuario objetivo: ").strip().title()  # pide y formatea el nombre
if usuario_objetivo not in usuarios:  # verifica si el nombre existe en la base
    print("Usuario no encontrado en la base de datos.")  # mensaje de error si no existe
    # termina la ejecución del script si el usuario no existe
    raise SystemExit  # sale del programa

# Solicita el umbral de similitud y maneja entradas inválidas
umbral_input = input("Ingrese umbral de similitud (0 a 1, por defecto 0.5): ").strip()  # pide el umbral al usuario
try:
    umbral = float(umbral_input) if umbral_input != "" else 0.5  # convierte a float o usa 0.5 si vacío
except ValueError:  # si la conversión falla
    print("Entrada inválida para el umbral, se usará 0.5 por defecto.")  # avisa del valor por defecto
    umbral = 0.5  # asigna un valor por defecto

# Llamada a la función que busca usuarios similares con el umbral especificado
similares = encontrar_usuarios_similares(usuario_objetivo, usuarios, umbral)  # obtiene la lista de similares

print(f"\nUsuarios similares a {usuario_objetivo}:")  # encabezado de salida de similares
for similar, similitud in similares:  # recorre la lista de similares obtenida
    print(f" {similar}: {similitud * 100:.0f}% similar")  # imprime cada similar con porcentaje

# Genera recomendaciones basadas en la lista de similares encontrada
recomendaciones = recomendar_contenido(usuario_objetivo, similares, usuarios)  # obtiene recomendaciones

print("\n" + "=" * 35)  # separador antes de mostrar recomendaciones finales
print("RECOMENDACIONES FINALES")  # título de la sección de recomendaciones
print("=" * 35)  # línea separadora

if recomendaciones:  # si existen recomendaciones
    for categoria, recomendadores in recomendaciones.items():  # recorre cada categoría recomendada
        print(f"\nCategoría: {categoria}")  # imprime el nombre de la categoría
        for recomendador, sim in recomendadores:  # recorre la lista de recomendadores para esa categoría
            print(f"  Recomendado por {recomendador} (similitud {sim})")  # imprime quién recomendó y su similitud
else:  # si no hay recomendaciones
    print("No hay recomendaciones disponibles.")  # muestra mensaje indicando ausencia de recomendaciones

print("\nEjecución finalizada.")  # mensaje de cierre del programa
