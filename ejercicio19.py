frutas = ["manzana", "pera", "naranja", "uva", "banano", "sandía", "pera"]  # lista inicial (hay duplicados)
print(f"Lista de frutas: {frutas}\n")  # muestra la lista y añade salto de línea
fruta_buscada = input("Ingrese una fruta que quiere buscar:\n").lower()  # pide input y convierte a minúsculas
if fruta_buscada in frutas:  # 'in' -> verifica si el valor existe en la lista
    print(f"\n{fruta_buscada} está en la lista")  # confirma existencia
    print(f"Primera aparición en posición: {frutas.index(fruta_buscada)}")  # index() devuelve la primera posición
    print(f"Aparece {frutas.count(fruta_buscada)} veces en total\n")  # count() cuenta todas las apariciones
else:
    print(f"{fruta_buscada} no está en la lista\n")  # avisa si no existe
buscadas = ["pera", "kiwi", "naranja"]# elementos a comprobar en la lista principal
print("Buscando múltiples frutas:", buscadas)# indica inicio de busqueda multiple
for fruta in buscadas:  # itera cada elemento de 'buscadas'
    if fruta in frutas:  # comprueba existencia para el elemento actual
        print(f"{fruta} encontrada en posición {frutas.index(fruta)}")  # muestra la primera posición encontrada
    else:
        print(f"{fruta} no encontrada")  # indica si el elemento no está
