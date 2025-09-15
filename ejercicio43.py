def merge_intervals(intervals):
    # Si no hay intervalos, devolvemos lista vacía
    if not intervals:
        return []
    # Ordenamos intervalos por inicio
    intervals_sorted = sorted(intervals, key=lambda x: x[0])
    merged = [intervals_sorted[0]]  # empezamos con el primer intervalo
    for current in intervals_sorted[1:]:
        prev = merged[-1]  # intervalo previo fusionable
        # Si se solapan (inicio actual <= fin previo) los fusionamos
        if current[0] <= prev[1]:
            # actualizamos el fin del prev al máximo entre ambos fines
            merged[-1] = (prev[0], max(prev[1], current[1]))
        else:
            merged.append(current)  # no solapan, añadimos actual como nuevo
    return merged

# Ejemplo
iv = [(1,3),(2,6),(8,10),(15,18)]
print("Merge:", merge_intervals(iv))
