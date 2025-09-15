numero = 1 # Empezamos desde 1
limite = int(input("escribe el limite en valor entero asi hallaremos entre ese rango cuales son pares:\n")) # Hasta dónde buscar
pares_encontrados = 0 # Contador de pares
print("Buscando números pares entre 1 y", limite, ":")
while numero <= limite:#ciclo con el limite que se digite
   if numero % 2 == 0: # % es el operador módulo (resto de división)
     print(numero, "es par")#imprime los numeros pares
     pares_encontrados = pares_encontrados + 1#suma de pares para que siga el ciclo
   numero = numero + 1#se suma hasta que se llegue al limite
print("Resumen:\nSe encontraron", pares_encontrados, "números pares")#imprime el resumen de pares encontrados