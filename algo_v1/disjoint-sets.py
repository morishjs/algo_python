parent = []
rank = []


def init():
    global parent,rank
    for i in range(0,5):
        parent.append(i)
        rank.append(0)

def union(p,q):
    global parent,rank
    p = find(p)
    q = find(q)
    if(p == q):
        return
    if(rank[p] > rank[q]):
        parent[q] = p
    else:
        parent[p] = q
        if(rank[p] == rank[q]):
            rank[q] += 1

def find(p):
    global parent,rank
    if(parent[p] == p):
        return p
    else:
        parent[p] = find(parent[p])
        return parent[p]



def main():
    init()
    union(0,1)

if __name__ == "__main__":
    main()