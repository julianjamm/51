nota = float(input("escribe tu nota para clasificar el rango:\n")) # Calificación del estudiante
if nota >= 9.0:#si nota es mayor o igual a 9
 clasificacion = "Excelente"#variable con texto excelente
 mensaje = "¡Felicidades! Sigue así"#variable con mensaje motivacional
elif nota >= 7.0: # elif significa "sino si", sies mayor o igual que 7 pero menor que 9 
 clasificacion = "Buena"#variable con texto Buena
 mensaje = "Buen trabajo, puedes mejorar"#variable con texto reconfortante
else:#entonces si es menor que 7 la nota
 clasificacion = "Necesita mejorar"#variable con texto que necesita mejorar
 mensaje = "Estudia más para la próxima"#variable con texto de esfuerzo
print("Tu nota es:", nota,"\nClasificación:", clasificacion,"\nComentario:", mensaje)#imprime lo anterior dependiendo la nota escoge