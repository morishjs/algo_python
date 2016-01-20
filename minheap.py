class node :
    def __init__(self, value, left=None, right=None, parent=None):
        self.left = node(left)
        self.right = node(right)
        self.parent = node(parent)
        self.value = value


class heap :
    def __init__(self,value):
        self.value = value
        self.root = node(value)
        self.nodeCount = 1
    def pop_node(self):
        pass
    def push_node(self,inValue):
        currentPos = self.root
        self.nodeCount += 1
        while(inValue >= currentPos.value):
            #adding dir func this here!
            if(dir == 0):
                currentPos = currentPos.left
            else: currentPos = currentPos.right
        #swap this here
        temp = currentPos
        

    def adjust_heap(self):
        pass



def main():
    #heap array
    arr = [3,2,4,5,0,3,7,1]

    root = heap(arr[0])

    for e in range(1,arr.count()):
        root.push_node(e)


