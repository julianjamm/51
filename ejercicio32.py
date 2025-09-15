import re  # Importar módulo de expresiones regulares para búsqueda de patrones

# Función para analizar características del texto
def analizar_texto(texto):
    """Analiza detalles básicos del texto"""
    info = {
        'total_caracteres': len(texto),  # Contar todos los caracteres
        'sin_espacios': len(texto.replace(' ', '')),  # Contar caracteres sin espacios
        'total_palabras': len(texto.split()),  # Contar palabras
        'total_oraciones': len([o for o in texto.split('.') if o.strip()]),  # Contar oraciones
        'total_parrafos': len([p for p in texto.split('\n\n') if p.strip()])  # Contar párrafos
    }
    return info  # Devolver diccionario de estadísticas

# Función para detectar emails
def buscar_emails(texto):
    """Encuentra correos electrónicos en el texto"""
    regex_email = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b'  # Patrón regex
    encontrados = re.findall(regex_email, texto)  # Buscar coincidencias
    return encontrados  # Retornar lista de emails

# Función para detectar teléfonos
def buscar_telefonos(texto):
    """Encuentra números telefónicos en varios formatos"""
    patrones = [
        r'\b\d{3}-\d{3}-\d{4}\b',  # Formato 123-456-7890
        r'\b\(\d{3}\)\s?\d{3}-\d{4}\b',  # Formato (123) 456-7890
        r'\b\d{10}\b'  # Formato 1234567890
    ]
    resultado = []  # Lista para almacenar teléfonos encontrados
    for p in patrones:  # Iterar patrones
        resultado.extend(re.findall(p, texto))  # Agregar coincidencias
    return resultado  # Retornar lista final

# Función de sentimiento simple
def analizar_sentimiento(texto):
    """Analiza sentimiento basado en palabras clave"""
    positivas = ['excelente', 'genial', 'fantástico', 'increíble', 'perfecto', 'bueno', 'feliz', 'contento', 'alegre', 'maravilloso']  # Lista positiva
    negativas = ['terrible', 'malo', 'horrible', 'triste', 'enojado', 'molesto', 'frustrado', 'decepcionado', 'pesimo']  # Lista negativa

    texto_lower = texto.lower()  # Convertir a minúsculas
    cuenta_pos = sum(1 for palabra in positivas if palabra in texto_lower)  # Contar positivas
    cuenta_neg = sum(1 for palabra in negativas if palabra in texto_lower)  # Contar negativas

    if cuenta_pos > cuenta_neg:  # Comparar
        estado = "Positivo"
    elif cuenta_neg > cuenta_pos:
        estado = "Negativo"
    else:
        estado = "Neutral"

    return {'sentimiento': estado, 'positivas': cuenta_pos, 'negativas': cuenta_neg}  # Devolver diccionario

# Función para encontrar palabras que se repiten
def palabras_repetidas(texto, min_len=4):
    """Detecta palabras repetidas de cierta longitud mínima"""
    lista_palabras = re.findall(r'\b\w+\b', texto.lower())  # Lista de palabras
    largas = [pal for pal in lista_palabras if len(pal) >= min_len]  # Filtrar por longitud
    freq = {}  # Diccionario para contar
    for pal in largas:
        freq[pal] = freq.get(pal, 0) + 1  # Contar repeticiones
    repetidas = {pal: f for pal, f in freq.items() if f > 1}  # Solo repetidas
    return repetidas  # Devolver resultado

# Función para mostrar estadísticas de manera legible
def mostrar_resumen(estadisticas):
    """Genera resumen legible de estadísticas"""
    est = estadisticas  # Alias para simplificar
    prom_pal_oracion = est['total_palabras'] / max(est['total_oraciones'], 1)  # Promedio palabras/oración
    resumen = []
    resumen.append(f"Total de caracteres: {est['total_caracteres']}")  # Agregar info
    resumen.append(f"Palabras: {est['total_palabras']} en {est['total_oraciones']} oraciones")  # Info
    resumen.append(f"Promedio palabras por oración: {prom_pal_oracion:.1f}")  # Promedio
    if est['total_parrafos'] > 1:
        resumen.append(f"Párrafos: {est['total_parrafos']}")  # Info de párrafos
    return resumen  # Retornar lista de resumen

# Función principal que integra todo
def analizar_completo(texto):
    """Realiza análisis completo del texto"""
    print("\n=== ANÁLISIS DE TEXTO ===")  # Encabezado
    estadisticas = analizar_texto(texto)  # Llamar función de estadísticas
    resumen = mostrar_resumen(estadisticas)  # Obtener resumen legible
    print("\n".join(resumen))  # Imprimir resumen

    emails = buscar_emails(texto)  # Buscar emails
    print(f"\nEmails detectados: {emails}")  # Mostrar emails

    telefonos = buscar_telefonos(texto)  # Buscar teléfonos
    print(f"Teléfonos detectados: {telefonos}")  # Mostrar teléfonos

    sentimiento = analizar_sentimiento(texto)  # Analizar sentimiento
    print(f"\nSentimiento general: {sentimiento['sentimiento']}")  # Mostrar sentimiento
    print(f"Palabras positivas: {sentimiento['positivas']}")  # Positivas
    print(f"Palabras negativas: {sentimiento['negativas']}")  # Negativas

    repetidas = palabras_repetidas(texto)  # Buscar palabras repetidas
    print(f"\nPalabras repetidas (≥4 letras): {repetidas}")  # Mostrar repetidas

# === EJEMPLO DE USO ===
if __name__ == "__main__":
    texto_usuario = input("Escribe el texto a analizar: ")  # Input del usuario
    analizar_completo(texto_usuario)  # Llamar función completa
