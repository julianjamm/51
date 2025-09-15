def sumar(a, b): return a + b
def restar(a, b): return a - b
def multiplicar(a, b): return a * b
def dividir(a, b): return a / b if b != 0 else "Error: No se puede dividir entre cero"

# Pedimos los números al usuario por separado
num1 = float(input("Escribe el primer número: "))
num2 = float(input("Escribe el segundo número: "))

print("\nCALCULADORA CON FUNCIONES")
print(f"Números a operar: {num1} y {num2}")
print("=" * 30)
print(f"{num1} + {num2} = {sumar(num1, num2)}")
print(f"{num1} - {num2} = {restar(num1, num2)}")
print(f"{num1} * {num2} = {multiplicar(num1, num2)}")
print(f"{num1} / {num2} = {dividir(num1, num2)}\n{'='*30}")
