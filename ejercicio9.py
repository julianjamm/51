numero_secreto = 7 # El número que hay que adivinar
adivinanza = int(input("escribe tu numero secreto: ")) # El número que el jugador eligió
print("El número secreto es:", numero_secreto,"\nTu adivinanza es:", adivinanza)
if adivinanza == numero_secreto: # == significa "es igual a"
 print("¡FELICIDADES! Adivinaste el número")
elif adivinanza < numero_secreto:# si adivinanza es menor que numero secreto
 print("Tu número es menor.\nIntenta con uno más grande")#imprime que es menor que el secreto
else:#si es ,ayor al numero secreto
 print("Tu número es mayor.\nIntenta con uno más pequeño")#imprime que es mayor