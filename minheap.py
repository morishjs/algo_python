class node :
    def __init__(self, value, position, left=None, right=None, parent=None):
        self.left = left
        self.right = right
        self.parent = parent
        self.value = value
        self.position = position


class heap :
    def __init__(self,value):
        self.value = value
        self.root = node(value,1)
        self.nodeCount = 1
    def pop_node(self):
        pass
    def push_node(self,inValue):
        currentPosNode = self.root
        self.nodeCount += 1
        parentNodeNum = int(self.nodeCount/2)

        #moving until currentPosNode = parentNodeNum.
        stack = []
        tmp = parentNodeNum
        if(tmp == self.root.position):
            if(self.nodeCount == 2):
                newNode = node(inValue,self.nodeCount,None,None,self.root)
                currentPosNode.left = newNode
            else :
                newNode = node(inValue,self.nodeCount,None,None,self.root)
                currentPosNode.right = newNode
            currentPosNode = newNode
        else:
            while(tmp != self.root.position):
                if(tmp % 2 == 0):
                    stack.append(0)
                else :
                    stack.append(1)
                tmp = tmp >> 1

            if(len(stack) != 0):
                lastdir = stack[0]

            while(currentPosNode.position != parentNodeNum):
                dir = stack.pop()
                if(dir == 0):
                    currentPosNode = currentPosNode.left
                else :
                    currentPosNode = currentPosNode.right


            newNode = node(inValue,self.nodeCount,None,None,currentPosNode)
            if(lastdir == 0):
                currentPosNode.left = newNode
            else : currentPosNode.right = newNode
            currentPosNode = newNode

        #bottom up
        while(currentPosNode.value < currentPosNode.parent.value and self.root != currentPosNode):
            temp = currentPosNode.value
            currentPosNode.value = currentPosNode.parent.value
            currentPosNode.parent.value = temp
            currentPosNode = currentPosNode.parent

def main():
    #heap array
    arr = [3,2,4,5,0,3,7,1]

    root = heap(arr[0])
    arr.pop(0)
    for e in arr:
        root.push_node(e)



if __name__ == "__main__":
    main()