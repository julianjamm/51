suma_total = 0 # Aquí guardaremos la suma
numero_actual = 1 # Empezamos desde el 1
limite = int(input("escribe el limite en valor entero:\n")) # Hasta qué número sumar
print(f"Sumando números del {numero_actual} al", limite)
while numero_actual <= limite:#ciclo hasta el limit que es 100
 suma_total = suma_total + numero_actual # Acumulamos la suma
 print("Sumando", numero_actual, "- Total hasta ahora:", suma_total)#imprime las sumas
 numero_actual = numero_actual + 1#hace operación de smarle al numero actual
print("Resultado final:\nLa suma de todos los números del 1 al", limite, "es:", suma_total)