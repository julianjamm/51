# Número fijo de materias
total_materias = 8
calificaciones = []  # Lista vacía para guardar las notas
print(f"Ingresa las calificaciones de {total_materias} materias:")
# Pedimos al usuario ingresar las notas una por una
for i in range(total_materias):
    nota = float(input(f"Calificación materia:\nnota maxima 10\n {i+1}: "))
    calificaciones.append(nota)
print("\nCalificaciones del estudiante:")
print(calificaciones)
# Estadísticas básicas
suma_notas = sum(calificaciones)  # suma de todas las notas
promedio = suma_notas / total_materias
nota_mayor = max(calificaciones)
nota_menor = min(calificaciones)
print(f"\n--- ESTADÍSTICAS ---")
print(f"Total de materias: {total_materias}\nSuma de todas las notas: {suma_notas}")
print(f"Promedio: {promedio:.2f}\nNota más alta: {nota_mayor}\nNota más baja: {nota_menor}")
# Contar notas aprobadas (>=7.0)
aprobadas = 0
for nota in calificaciones:
    if nota >= 7.0:
        aprobadas += 1
print(f"Materias aprobadas: {aprobadas} de {total_materias}")