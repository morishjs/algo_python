graph = {'A': set(['B', 'C']),
         'B': set(['A', 'D', 'E']),
         'C': set(['A', 'F']),
         'D': set(['B']),
         'E': set(['B', 'F']),
         'F': set(['C', 'E'])}



def BFS(graph, start):
    visited,queue = set(), [start]
    path = []
    while(len(queue) != 0):
        node = queue.pop(0)
        if node not in visited:
            
            visited.add(node)
            queue.extend(graph[node]-visited)

    return visited


print BFS(graph,'A')
