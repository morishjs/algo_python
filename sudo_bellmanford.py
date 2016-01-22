graph = {'S': set(['A', 'E']),
         'A': set(['S','C']),
         'B': set(['A']),
         'C': set(['B']),
         'D': set(['A', 'C']),
         'E': set(['D'])}
edges = {('S','E') : 8,
         ('S','A'): 10,
         ('A','C'): 2,
         ('A','S'): -20,
         ('B','A'): 1,
         ('C','B'): -2,
         ('D','A'):-4,
         ('D','C'):-1,
         ('E','D'): 1
          }



def BellmanFord(i,j):
    distance = {}
    cycle = False
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

    previous = distance[j]
    print previous

    #iteration once again
    for edge in edges.keys():
        #u = edgesource
        u = edge[0]
        #v = edgedestination
        v = edge[1]

        if(distance[u] + edges[(u,v)] < distance[v]):
            distance[v] = distance[u] + edges[(u,v)]

    print distance[j]
    if(previous > distance[j]):
        cycle = True


    return cycle

i = 'S'
j = 'B'
print BellmanFord('S','B')

