# Является ли граф деревом


# Не дерево
graph = {
    1: [2, 3],
    2: [1, 3],
    3: [1, 2], 
    4: [6, 7], 
    5: [6, 7], 
    6: [4, 5, 7], 
    7: [4, 5, 6], 
    8: [11],
    9: [10, 11], 
    10: [9], 
    11: [8, 9]
}

tree = {
    1: [2, 3, 4],
    2: [],
    3: [],
    4: [5],
    5: []
}

def IsTree(graph, start):
    visited = []
    queue = [start]
    parent = {start: None}

    while queue:
        vertex = queue.pop()
        visited.append(vertex)
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                queue.append(neighbor)
                parent[neighbor] = vertex
            else:
                if parent[vertex] != neighbor:
                    return False
    
    return len(visited) == len(graph)



print(IsTree(graph, 1))


print(IsTree(tree, 1))
