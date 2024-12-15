def sort_edges_by_start_vertex(edges):
    # Сортируем рёбра по начальной вершине
    edges.sort(key=lambda edge: edge[0])
    return edges

# Пример данных
edges = [(3, 5), (1, 4), (2, 6), (1, 2), (4, 5)]

# Вызов функции сортировки
sorted_edges = sort_edges_by_start_vertex(edges)

# Вывод результата
print("Отсортированные рёбра:", sorted_edges)
