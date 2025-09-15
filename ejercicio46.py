def rotar_matriz(m):
    # Asumimos matriz cuadrada
    n = len(m)  # tamaño de la matriz
    # Rotamos por capas (desde fuera hacia dentro)
    for layer in range(n // 2):
        first = layer
        last = n - 1 - layer
        for i in range(first, last):
            offset = i - first
            # guardamos top
            top = m[first][i]
            # left -> top
            m[first][i] = m[last - offset][first]
            # bottom -> left
            m[last - offset][first] = m[last][last - offset]
            # right -> bottom
            m[last][last - offset] = m[i][last]
            # top -> right
            m[i][last] = top

# Ejemplo
mat = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
rotar_matriz(mat)
print("Matriz rotada 90°:")
for row in mat:
    print(row)
