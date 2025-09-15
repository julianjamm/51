import heapq  # usamos heapq para eficiencia

def kth_mas_grande(nums, k):
    # Si k es mayor que la cantidad de elementos devolvemos None
    if k > len(nums) or k <= 0:
        return None
    # Usamos un heap mínimo de tamaño k
    heap = []
    for n in nums:
        if len(heap) < k:
            heapq.heappush(heap, n)  # añadimos elemento al heap
        else:
            # si el elemento es mayor que el mínimo del heap, lo reemplazamos
            if n > heap[0]:
                heapq.heapreplace(heap, n)
    return heap[0]  # el root del heap es el k-ésimo más grande

# Ejemplo de uso
nums = [7,4,6,3,9,1,2,8]
print("Lista:", nums)
print("3er más grande:", kth_mas_grande(nums, 3))
