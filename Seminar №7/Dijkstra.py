import math
# Алгоритм Дейкстры 

# Вспомогательная функция для нахождения вершины с минимальным расстоянием
def VertexWithMinWeight(visited, dist):
    min_weight = float('inf')
    min_vertex = None
    for vertex in dist:
        # Eсли текущее расстояние меньше минимального и вершина не посещена
        if not visited[vertex] and dist[vertex] < min_weight:
            min_weight = dist[vertex]
            # Oбновляем индекс вершины с минимальным значением
            min_vertex = vertex
    return min_vertex


def Dijkstra(graph, start):
    #Создаем словарь для отслеживания посещенных вершин 
    # Для каждой вершины проставляем false
    visited = {vertex: False for vertex in graph}

    # Создаем словарь для хранения расстояний до каждой вершины в графе
    dist = {vertex: float('inf') for vertex in graph}

    # Расстояние до начальной вершины равно 0
    dist[start] = 0


    # Пока есть не посещенные вершины
    while False in visited.values():
        # Находим вершину с минимальным расстоянием
        u = VertexWithMinWeight(visited, dist)

        visited[u] = True
        # Перебираем всех соседей вершины u     
        for neighbor, weight in graph[u].items():
            # Вычисляем новое расстояние до соседа через текущую вершину
            new_dist = dist[u] + weight

            # Если новое расстояние меньше текущего кратчайшего расстояния до соседа
            if new_dist < dist[neighbor]:

                # Обновляем кратчайшее расстояние до соседа
                dist[neighbor] = new_dist

    return dist


graph = {
    'A': {'B': 5, 'C': 3},
    'B': {'C': 2, 'D': 6},
    'C': {'D': 7, 'E': 4},
    'D': {'E': 1},
    'E': {}
}

print(Dijkstra(graph, "A"))