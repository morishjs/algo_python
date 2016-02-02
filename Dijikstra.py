#Dijikstra algo
from collections import defaultdict
from heapq import *

def dijikstra( nodes, edges ):
    conn = defaultdict(list)
    distance = {}
    for n1,n2,c in edges:
        conn[ n1 ].append( (c, n1, n2) )
        conn[ n2 ].append( (c, n2, n1) )


    used = set( nodes[ 0 ] ) # used = "A" nodes[0] = "A"
    usable_edges = conn[nodes[0]]

    for i in nodes:
        if i == nodes[0]:
            distance[i] = 0
        else:     distance[i] = 255

    for e in conn[nodes[0]]:
        distance[e[2]] = e[0]



    heapify( usable_edges )

    while usable_edges:
        cost, n1, vnear = heappop( usable_edges )
        if vnear not in used:
            used.add(vnear)

            for e in conn[vnear]:
                if e[2] not in used:
                    if(distance[vnear] + cost < distance[e[2]]):
                        distance[e[2]] = distance[vnear] + cost
                    heappush( usable_edges, e )


    return distance




#test
nodes = list("ABCDEFG")
edges = [ ("A", "B", 7), ("A", "D", 5),
          ("B", "C", 8), ("B", "D", 9), ("B", "E", 7),
      ("C", "E", 5),
      ("D", "E", 15), ("D", "F", 6),
      ("E", "F", 8), ("E", "G", 9),
      ("F", "G", 11)]

print "Dijikstra algo_Shortest weight:", dijikstra( nodes, edges )