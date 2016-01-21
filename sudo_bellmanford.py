graph = {'S': set(['A', 'E']),
         'A': set(['C']),
         'B': set(['A']),
         'C': set(['B']),
         'D': set(['A', 'C']),
         'E': set(['D'])}
edges = {('S','E') : 8,
         ('S','A'): 10,
         ('A','C'): 2,
         ('B','A'): 1,
         ('C','B'): -2,
         ('D','A'):-4,
         ('D','C'):-1,
         ('E','D'): 1
          }



def BellmanFord():
    distance = {}
    for node in graph.keys():
        if(node == 'S'):
            distance[node] = 0
        else :
            distance[node] = 255

    for node in graph.keys():
        for edge in edges.keys():
            #u = edgesource
            u = edge[0]
            #v = edgedestination
            v = edge[1]

            if(distance[u] + edges[(u,v)] < distance[v]):
                distance[v] = distance[u] + edges[(u,v)]

    return distance

print BellmanFord()

