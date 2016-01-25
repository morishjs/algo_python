#An independent set of a graph is a subset of vertices in the graph such that no two vertices in the set are adjacent
#Given a tree, design an efficient algorithm that computes a maximum independent set of T and analyze the running
#time of your algorithm.


class Node :
    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right



def independent_set(root,e_root,i_root):

    if(root == None):
        return 0

    if(root.left):
        e_root += independent_set(root.left,e_root,i_root)
    if(root.right):
        e_root += independent_set(root.right,e_root,i_root)

    if(root.left):
        i_root += independent_set(root.left.left,e_root,i_root) + independent_set(root.left.right,e_root,i_root) + 1
    if(root.right):
        i_root += independent_set(root.right.left,e_root,i_root) + independent_set(root.right.right,e_root,i_root) + 1

    return max(e_root,i_root)



def main():
    root = Node()
    root.left = Node(Node())
    root.right = Node(Node(),Node())

    print independent_set(root,0,0)

if __name__ == "__main__" :
    main()

