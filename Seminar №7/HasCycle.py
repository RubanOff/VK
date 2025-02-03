def HasCycle(graph):
    visited = []
    for vertex in graph:
        if vertex not in visited:
            if DFS(graph, vertex, None, visited):
                return True
    return False

def DFS(graph, vertex, parent, visited):
    visited.append(vertex)
    for neighbor in graph[vertex]:
        if neighbor != parent:
            if neighbor in visited or DFS(graph, neighbor, vertex, visited):
                return True
            
    return False

graph = {
1: [2, 3], 2: [1, 3], 3: [1, 2], 4: [6, 7], 5: [6, 7], 6: [4, 5, 7], 7: [4, 5, 6], 8: [11],
9: [10, 11], 10: [9], 11: [8, 9]
}

print(HasCycle(graph))