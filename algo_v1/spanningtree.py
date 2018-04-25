from collections import defaultdict
from heapq import *
 
def prim( nodes, edges ):
    conn = defaultdict(list)
    for n1,n2,c in edges:
        conn[ n1 ].append( (c, n1, n2) )
        conn[ n2 ].append( (c, n2, n1) )

    mst = []
    used = set( nodes[ 0 ] ) # used = "A" nodes[0] = "A"
    usable_edges = conn[nodes[0]]


    heapify( usable_edges )

    while usable_edges:
        cost, n1, n2 = heappop( usable_edges )
        if n2 not in used:
            used.add(n2)
            mst.append((n1, n2, cost))
 
            for e in conn[n2]:
                if e[2] not in used:
                    heappush( usable_edges, e )
    return mst

def kruskal(nodes, edges):
    conn = defaultdict(list)
    alledges = []
    visited = []
    mst = []

    for n1,n2,w in edges:
        conn[n1].append((w,n1,n2))
    for n in nodes:
        alledges.extend(conn[n])

    heapify(alledges)

    while(len(mst)+1 != len(nodes)):

        edge = heappop(alledges)
        t1 = findDisjoint(edge[1],visited)
        t2 = findDisjoint(edge[2],visited)
        if(t1 != t2):
            if(len(t1)>1):
                visited.remove(t1)
            if(len(t2)>1):
                visited.remove(t2)
            visited.append(t1 | t2)
            mst.append(edge)


    return mst

def findDisjoint(e, visited):
    for s in visited:
        if e in s:
            return s
    return set(e)


#test
nodes = list("ABCDEFG")
edges = [ ("A", "B", 7), ("A", "D", 5),
          ("B", "C", 8), ("B", "D", 9), ("B", "E", 7),
      ("C", "E", 5),
      ("D", "E", 15), ("D", "F", 6),
      ("E", "F", 8), ("E", "G", 9),
      ("F", "G", 11)]
 
print "prim:", prim( nodes, edges )
print "kruskal:", kruskal(nodes,edges)