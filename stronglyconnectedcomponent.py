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
    Topological=[]

    while len(stack) != 0 :
        e = stack.pop()

        if(e not in visited):
            path.append(e)
            visited.add(e)

            remain = graph[e]-visited
            if remain == set():
                Topological.append(e)
                prev = path[-2]
                for before in graph(prev)-visited:
                    if(before == set()):
                        Topological.append(before)
                        prev = path[path.index(prev)-1]
                    else : break

            for vertex in graph[e]:
                if vertex not in visited:
                    stack.append(vertex)

    return Topological



print DFS(graph,'A')
