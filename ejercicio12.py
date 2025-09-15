numero = float(input("escribe el numero que desees saber la tabla de multiplicar:\n")) # Número para la tabla
multiplicador = 0 # Empezamos multiplicando por 0
print(f"Tabla de multiplicar del", numero, ":\n","=" * 25)# imprime titulo mas el numero que se digito en input y barra decorativa
while multiplicador <= 10:#siclo hasta el 10 de la tabla de multiplicar con el numero escrito
 resultado = numero * multiplicador#variable que hace operacion de multiplicar
 print(numero, "x", multiplicador, "=", resultado)#imprime el numero escogido con un x de multiplicar y la secuencia hasta el 10 con su resultado
 multiplicador = multiplicador + 1# aca le va sumando al multiplicador para que la secuencia siga hasta 10
print("=" * 25,"\n¡Tabla completa!")#imprime el final con barra decorativa
