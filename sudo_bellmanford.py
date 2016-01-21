
def BellmanFord():

    for i in node:
        if(i == source):
            distance[i] = 0
        else :
            distance[i] = 255

    for i in edges:
        for k in nodes:
            if(distance[k] + W[k][i] < distance[i]):
                distance[i] = distance[k] + W[k][i]

    #cycle check
    for j in nodes:
        if(distance[j] + W[j][dest] < distance[dest]):
            cycle_exist = true


