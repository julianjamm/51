# Función optimizada para verificar si un número es primo (método básico pero sin prints internos)
def es_primo_simple(numero):                                 # Define la función que recibe un entero 'numero'
    # Si el número es menor que 2 no puede ser primo
    if numero < 2:                                          # Comprueba si el número es menor que 2
        return False                                       # Retorna False porque 0 y 1 no son primos
    # Calcula la raíz entera para limitar las comprobaciones
    raiz = int(numero ** 0.5)                               # Calcula la raíz cuadrada entera de 'numero'
    # Prueba divisores solo hasta la raíz cuadrada
    for divisor in range(2, raiz + 1):                      # Recorre posibles divisores desde 2 hasta la raíz
        if numero % divisor == 0:                           # Si 'numero' es divisible por 'divisor'
            return False                                   # No es primo, retorna False
    # Si no se encontró divisor, entonces es primo
    return True                                            # Retorna True indicando que es primo

# Función optimizada de la Criba de Eratóstenes que devuelve lista de primos
def criba_eratostenes(limite):                             # Define la función que recibe el límite superior
    # Si el límite es menor que 2 no hay primos
    if limite < 2:                                         # Comprueba si el límite es menor que 2
        return []                                          # Devuelve lista vacía porque no hay primos
    # Inicializa array booleano donde True significa "posible primo"
    es_primo = [True] * (limite + 1)                       # Crea lista de True de tamaño limite+1
    es_primo[0] = es_primo[1] = False                      # Marca 0 y 1 como no primos
    # Recorre hasta la raíz para marcar múltiplos
    tope = int(limite ** 0.5)                              # Calcula la raíz cuadrada entera del límite
    for i in range(2, tope + 1):                           # Recorre cada i posible hasta la raíz
        if es_primo[i]:                                    # Si i todavía está marcado como primo candidato
            # Marca los múltiplos de i comenzando en i*i como no primos
            for j in range(i * i, limite + 1, i):          # Recorre múltiplos de i desde i*i hasta limite
                es_primo[j] = False                        # Marca el múltiplo como no primo
    # Construye y retorna la lista de índices (números) que quedaron True (primos)
    return [numero for numero, primo in enumerate(es_primo) if primo]  # Lista por comprensión con los primos

# Función para factorizar un número en sus factores primos
def factorizacion_prima(numero):                           # Define la función que recibe el entero 'numero'
    # Manejo de casos triviales
    if numero < 2:                                         # Si el número es menor que 2
        return []                                          # No tiene factores primos significativos
    factores = []                                          # Lista donde se guardarán los factores primos
    n = numero                                             # Copia del número para operar sin perder el original
    divisor = 2                                            # Comenzamos probando con el divisor 2
    # Repetimos hasta que divisor^2 sea mayor que el valor restante
    while divisor * divisor <= n:                          # Mientras divisor^2 <= n
        while n % divisor == 0:                            # Mientras 'n' sea divisible por 'divisor'
            factores.append(divisor)                       # Añadimos el divisor a la lista de factores
            n //= divisor                                  # Dividimos n por divisor (reducción)
        divisor += 1                                       # Pasamos al siguiente posible divisor
    # Si queda un número mayor que 1 al final, es un factor primo restante
    if n > 1:                                              # Si el residuo final es mayor que 1
        factores.append(n)                                 # Lo añadimos como factor primo final
    return factores                                        # Devolvemos la lista de factores primos

# ------------------- PROGRAMA PRINCIPAL (interactivo) -------------------
print("GENERADOR Y HERRAMIENTAS DE NÚMEROS PRIMOS")         # Titular del programa
print("=" * 48)                                           # Línea separadora visual

# Entrada 1: Verificación individual de primos (múltiples valores opcionales)
entrada_primos = input("Ingrese números separados por comas para verificar si son primos (ej: 17,25,29) o presione Enter para omitir:\n> ")
# Si el usuario escribió algo, procesamos la lista, si no, se omite esta sección
if entrada_primos.strip():                                # Comprueba si la entrada no está vacía
    try:                                                  # Intentamos convertir cada elemento a entero
        lista_probar = [int(x.strip()) for x in entrada_primos.split(",") if x.strip() != ""]  # Lista de enteros
    except ValueError:                                    # Si alguna conversión falla
        print("Error: asegúrate de ingresar solo números enteros separados por comas.")          # Mensaje de error
        lista_probar = []                                 # Lista vacía si hubo error
    # Para cada número solicitado, mostramos si es primo usando la función optimizada
    if lista_probar:                                      # Si hay números válidos para probar
        print("\n1. COMPROBACIÓN INDIVIDUAL DE PRIMOS")   # Título de la sección
        for num in lista_probar:                         # Recorre cada número ingresado
            es_primo = es_primo_simple(num)              # Llama a la función es_primo_simple
            print(f"{num}: {'Primo' if es_primo else 'No primo'}")  # Muestra resultado claro

# Entrada 2: Límite para la Criba de Eratóstenes (obligatorio interactivo)
limite_input = input("\nIngrese el límite entero para la Criba de Eratóstenes (ej: 30). Presione Enter para usar 30 por defecto:\n> ")
# Procesamos la entrada del límite con manejo de error
try:
    limite = int(limite_input) if limite_input.strip() else 30  # Usa 30 si se presiona Enter sin valor
except ValueError:
    print("Entrada inválida para el límite, se usará 30 por defecto.")  # Mensaje si no es entero
    limite = 30                                                     # Valor por defecto

# Ejecutamos la criba y mostramos resultados
primos_encontrados = criba_eratostenes(limite)                    # Llama a la función criba_eratostenes
print(f"\n2. CRIBA DE ERATÓSTENES hasta {limite}")                  # Título de la sección
print(f"Primos encontrados: {primos_encontrados}")                 # Muestra la lista de primos
print(f"Total de primos: {len(primos_encontrados)}")               # Muestra cuántos primos se encontraron

# Entrada 3: Número para factorización prima (interactivo)
factor_input = input("\nIngrese un número entero para factorizar (ej: 60) o presione Enter para omitir:\n> ")
# Si el usuario dio un número válido, hacemos la factorización y verificación
if factor_input.strip():                                           # Comprueba que la entrada no esté vacía
    try:
        numero_factorizar = int(factor_input)                      # Intenta convertir a entero
        factores = factorizacion_prima(numero_factorizar)          # Llama a la función de factorización
        # Muestra la factorización en formato multiplicativo
        if factores:                                               # Si hay factores devueltos
            factores_str = " × ".join(map(str, factores))          # Une factores con el símbolo ×
            print(f"\n3. FACTORIZACIÓN PRIMA de {numero_factorizar}:")  # Título para la factorización
            print(f"{numero_factorizar} = {factores_str}")         # Muestra la factorización completa
            # Verificación multiplicativa simple
            producto = 1                                           # Inicializa verificador producto
            for f in factores:                                     # Recorre factores
                producto *= f                                      # Multiplica sucesivamente
            print(f"Verificación: {factores_str} = {producto}")     # Muestra que la multiplicación da el original
        else:
            print("No se encontraron factores (entrada inválida o número < 2).")  # Mensaje si no hay factores
    except ValueError:
        print("Error: la factorización requiere un número entero válido.")         # Mensaje si la entrada no es un entero

print("\nEjecución finalizada.")                                     # Mensaje final de cierre
print("=" * 48)                                                   # Línea separadora final