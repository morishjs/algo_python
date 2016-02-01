#This algorithm includes 'Topological algorithm' , DFS and strongly connected component.

graph = {'A': set(['B', 'C']),
         'B': set(['D', 'E']),
         'C': set(['F']),
         'D': set(),
         'E': set(['F']),
         'F': set(['E'])}



def DFS(graph, start):
    visited = set()
    stack = [start]
    path = []
    parent = {}
    Topological=[]

    while len(stack) != 0 :
        e = stack.pop()

        if(e not in visited):
            path.append(e)
            visited.add(e)

            for vertex in graph[e]:
                if vertex not in visited:
                    stack.append(vertex)
                    parent[vertex] = e

            if graph[e] - visited == set():
                Topological.append(e)
                prevnode = parent[e]
                debug = graph[prevnode] - visited
                while graph[prevnode] - visited == set():
                    Topological.append(prevnode)
                    if prevnode != start:
                        prevnode = parent[prevnode]
                    else: return Topological




print DFS(graph,'A')
