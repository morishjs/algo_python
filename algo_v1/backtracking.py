class node:
    pass

def promising(node):
    pass

def main():
    answer = "user input"
    back_tracking(0,answer)

def back_tracking(index,answer):
    node u = node()
    if(promising(u)) :
        if(answer == u):
            return True
        else :
            for in u.child:
                back_tracking(index+1,answer)



if __name__ == "__main__":
    main()