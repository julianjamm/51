registro_alumnos = []

def registrar_alumno(nombre, edad, curso):
    """Registra un nuevo alumno en el sistema"""
    alumno = {  # Creamos un diccionario con la información del alumno
        "nombre_completo": nombre,  # Nombre del alumno
        "edad": edad,  # Edad del alumno
        "curso": curso,  # Grado o curso del alumno
        "notas": []  # Lista vacía para guardar las calificaciones
    }
    registro_alumnos.append(alumno)  # Agregamos el alumno a la lista global
    print(f"✔ Estudiante {nombre} agregado exitosamente")  # Confirmación

def localizar_alumno(nombre):
    """Busca la posición de un alumno por nombre"""
    for i, alumno in enumerate(registro_alumnos):  # Recorremos la lista de alumnos
        if alumno["nombre_completo"].lower() == nombre.lower():  # Comparación sin importar mayúsculas
            return i  # Retorna la posición del alumno si existe
    return -1  # Si no existe retorna -1

def añadir_nota(nombre, materia, valor):
    """Agrega una calificación a un alumno existente"""
    pos = localizar_alumno(nombre)  # Buscamos al alumno
    if pos != -1:  # Si se encontró
        calificacion = {"materia": materia, "valor": valor}  # Creamos un diccionario con la nota
        registro_alumnos[pos]["notas"].append(calificacion)  # Guardamos la nota en el alumno
        print(f"✔ Calificación agregada a {nombre}: {materia} = {valor}")  # Confirmación
    else:
        print(f"✘ Estudiante {nombre} no encontrado")  # Mensaje de error si no existe

def promedio_alumno(nombre):
    """Calcula el promedio de las calificaciones de un alumno"""
    pos = localizar_alumno(nombre)  # Buscamos al alumno
    if pos != -1:  # Si se encontró
        notas = registro_alumnos[pos]["notas"]  # Obtenemos sus notas
        if notas:  # Si tiene notas registradas
            suma = sum(n["valor"] for n in notas)  # Sumamos todas las notas
            return round(suma / len(notas), 2)  # Calculamos promedio con 2 decimales
        else:
            return 0  # Si no tiene notas registradas
    return None  # Si no existe el alumno

def mostrar_reporte():
    """Muestra un reporte completo con todos los alumnos"""
    print("\n" + "="*50)  # Línea decorativa
    print("REPORTE DE ESTUDIANTES")  # Título
    print("="*50)  # Línea decorativa

    if not registro_alumnos:  # Si no hay estudiantes en la lista
        print("✘ No hay estudiantes registrados aún")  # Aviso
        return

    for alumno in registro_alumnos:  # Recorremos todos los alumnos
        print(f"\nNombre: {alumno['nombre_completo']}")  # Mostramos nombre
        print(f"Edad: {alumno['edad']} años")  # Mostramos edad
        print(f"Grado: {alumno['curso']}°")  # Mostramos grado
        if alumno["notas"]:  # Si tiene notas registradas
            print("Calificaciones:")
            for n in alumno["notas"]:  # Recorremos sus notas
                print(f" - {n['materia']}: {n['valor']}")  # Mostramos cada materia y nota
            promedio = promedio_alumno(alumno["nombre_completo"])  # Calculamos promedio
            print(f"Promedio general: {promedio}")  # Mostramos promedio
        else:
            print("Sin calificaciones registradas")  # Si no tiene notas
        print("-" * 30)  # Separador visual

def buscar_alumno():
    """Permite buscar y mostrar un estudiante específico"""
    nombre = input("Ingrese el nombre del estudiante a buscar: ")  # Pedimos el nombre
    pos = localizar_alumno(nombre)  # Buscamos la posición del alumno
    if pos != -1:  # Si se encontró
        alumno = registro_alumnos[pos]  # Obtenemos sus datos
        print(f"\n✔ Estudiante encontrado: {alumno['nombre_completo']}")  # Confirmación
        print(f"Edad: {alumno['edad']} años")  # Mostramos edad
        print(f"Grado: {alumno['curso']}")  # Mostramos curso
        if alumno["notas"]:  # Si tiene notas registradas
            print("Calificaciones:")
            for n in alumno["notas"]:  # Recorremos notas
                print(f" - {n['materia']}: {n['valor']}")  # Mostramos cada una
            promedio = promedio_alumno(alumno["nombre_completo"])  # Calculamos promedio
            print(f"Promedio general: {promedio}")  # Mostramos promedio
        else:
            print("Sin calificaciones registradas")  # Si no tiene notas
    else:
        print(f"✘ Estudiante {nombre} no encontrado")  # Si no se encuentra


# =======================
# MENÚ PRINCIPAL
# =======================
def menu():
    print("SISTEMA DE REGISTRO DE ESTUDIANTES")  # Título inicial
    while True:  # Ciclo infinito hasta que se elija salir
        print("\n=== MENÚ ===")  # Menú de opciones
        print("1. Registrar estudiante")  
        print("2. Agregar calificación")
        print("3. Buscar estudiante")
        print("4. Mostrar reporte")
        print("5. Salir")

        opcion = input("Seleccione una opción: ")  # Pedimos al usuario que elija

        if opcion == "1":  # Registrar estudiante
            nombre = input("Nombre del estudiante: ")
            edad = int(input("Edad: "))
            curso = input("Grado: ")
            registrar_alumno(nombre, edad, curso)

        elif opcion == "2":  # Agregar calificación
            nombre = input("Nombre del estudiante: ")
            materia = input("Materia: ")
            try:
                nota = float(input("Nota: "))  # Se valida que la nota sea numérica
            except ValueError:
                print("✘ Error: la nota debe ser numérica")  # Si no es número
                continue
            añadir_nota(nombre, materia, nota)

        elif opcion == "3":  # Buscar estudiante
            buscar_alumno()

        elif opcion == "4":  # Mostrar reporte
            mostrar_reporte()

        elif opcion == "5":  # Salir
            print("✔ Saliendo del sistema...")
            break  # Rompe el bucle y termina el programa

        else:  # Si elige una opción incorrecta
            print("✘ Opción inválida, intente de nuevo")


# Ejecutar menú
menu()  # Llama a la función principal para iniciar el sistema
