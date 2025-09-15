from collections import Counter  # Contar frecuencia de caracteres
import heapq  # Para manejo de heap (cola de prioridad)

# Clase nodo para Huffman
class NodoHuffman:
    """Nodo que representa un carácter y su frecuencia"""
    def __init__(self, caracter, frecuencia, izq=None, der=None):
        self.char = caracter  # Guardar caracter
        self.freq = frecuencia  # Guardar frecuencia
        self.left = izq  # Hijo izquierdo
        self.right = der  # Hijo derecho

    def __lt__(self, otro):
        """Comparar nodos para heap basado en frecuencia"""
        return self.freq < otro.freq

# Función de compresión básica por repeticiones consecutivas
def comprimir_repeticiones(texto):
    """Comprime repeticiones consecutivas de caracteres"""
    comprimido = ""  # Inicializar texto comprimido
    cuenta = 1  # Contador de repeticiones
    for i in range(1, len(texto)):  # Iterar desde el segundo caracter
        if texto[i] == texto[i-1]:  # Si es igual al anterior
            cuenta += 1  # Incrementar contador
        else:
            if cuenta > 1:  # Si hubo repeticiones
                comprimido += str(cuenta) + texto[i-1]  # Agregar número + caracter
            else:
                comprimido += texto[i-1]  # Agregar solo el caracter
            cuenta = 1  # Reiniciar contador
    # Agregar último caracter
    if cuenta > 1:
        comprimido += str(cuenta) + texto[-1]
    else:
        comprimido += texto[-1]
    return comprimido  # Retornar texto comprimido

# === BLOQUE PRINCIPAL ===
if __name__ == "__main__":
    texto_usuario = input("Ingrese un texto para comprimir: ")  # Input del usuario
    resultado_comprimido = comprimir_repeticiones(texto_usuario)  # Comprimir texto
    print("\nTexto original:")  # Mostrar texto original
    print(texto_usuario)
    print("\nTexto comprimido:")  # Mostrar resultado
    print(resultado_comprimido)
