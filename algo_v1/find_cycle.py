graph = {'A': set(['B', 'C']),
         'B': set(['A', 'D', 'E']),
         'C': set(['A', 'F']),
         'D': set(['B','F']),
         'E': set(['B']),
         'F': set(['C','D'])}

parent = {'A': set(),
          'B': set(),
          'C': set(),
          'D': set(),
          'E': set(),
          'F': set()
          }

def DFS(graph, start):
    visited, stack = set(),[start]
    path = []
    cycle = False
    while stack :
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            for e in graph[vertex]:
                if e in visited:
                    if set(e) != parent[vertex]:

                        cycle = True


            path.append(vertex)
            stack.extend(graph[vertex]-visited)
            for child in graph[vertex]:
                parent[child].add(vertex)

    return cycle


if __name__ == "__main__":
    print DFS(graph, 'A')