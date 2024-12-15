import heapq

def dijkstra(graph, start):
    # Устанавливаем начальные расстояния до всех узлов
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)

        # Игнорируем, если расстояние не соответствует текущему
        if current_distance > distances[current_vertex]:
            continue

        # Обновляем расстояния до соседних вершин
        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight

            # Если найден более короткий путь
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances

# Пример графа
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}

# Запуск алгоритма
start_vertex = 'A'
distances = dijkstra(graph, start_vertex)

print("Расстояния от вершины", start_vertex, "до других вершин:")
for vertex, distance in distances.items():
    print(f"{vertex}: {distance}")
