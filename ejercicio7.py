precio_total = float(input("escribe el total de tu compra:\n")) # Total de la compra
descuento = 0 # Inicializamos el descuento en 0
if precio_total >= 100: # Si gasta más de $100
 descuento = precio_total * 0.10 # 10% de descuento
 precio_final = precio_total - descuento#relta el precio con el descuento si supera $100
 print("¡Felicidades! Tienes un descuento del 10%\nDescuento aplicado: $", descuento)#imprime
else:#sino
 precio_final = precio_total#si el precio es menor que 100 no aplica descuento
print("No hay descuento disponible\nPrecio original: $", precio_total,"\nPrecio final: $", precio_final)#imprime
