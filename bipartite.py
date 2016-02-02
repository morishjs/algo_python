#bipartite
graph = {'A': set(['B', 'C']),
         'B': set(['D', 'E']),
         'C': set(['F']),
         'D': set(),
         'E': set(['F']),
         'F': set()}

color = {}
#check B has C? or C has B?

def BFS(graph, start):
    visited,queue = set(), [start]
    color[start] = 0
    brother = []
    bipartite = True

    for node in graph.keys():
        color[node] = -1

    while(len(queue) != 0):
        node = queue.pop(0)

        if node not in visited:
            visited.add(node)

            for brother in graph[node]:
                if color[brother] == -1:
                    if color[node] == 0:
                        color[brother] = 1
                    else: color[brother] = 0
                else :
                    if color[brother] == color[node]:
                        bipartite = False
            #queue.extend(graph[node]-visited)
            queue.extend(graph[node])



    return bipartite


print BFS(graph,'A')
