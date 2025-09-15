def mediana(nums):
    # Si la lista está vacía devolvemos None
    if not nums:
        return None
    nums_sorted = sorted(nums)  # ordenamos la lista
    n = len(nums_sorted)  # cantidad de elementos
    mid = n // 2  # índice medio
    if n % 2 == 1:
        # si impar, la mediana es el elemento central
        return nums_sorted[mid]
    else:
        # si par, es el promedio de los dos centrales
        return (nums_sorted[mid - 1] + nums_sorted[mid]) / 2

# Ejemplo
print("Mediana [3,1,2]:", mediana([3,1,2]))
print("Mediana [4,1,2,3]:", mediana([4,1,2,3]))
