# Дан граф. Необходимо подсчитать количество компонент связности.

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

def FindConnectedComponents(graph):

    visited = {}
    for i in graph:
        visited[i] = False
    
    connected_components = []

    for v in graph:
        if not visited[v]:
            component = []
            DFS(graph, v, visited, component)
            connected_components.append(component)


    return connected_components




def DFS(graph, v, visited, component):
    visited[v] = True
    component.append(v)
    for v in graph[v]:
        if not visited[v]:
            DFS(graph, v, visited, component)


print(FindConnectedComponents(graph))




