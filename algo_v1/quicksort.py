def quicksort(arr, left, right):

    if(left < right):
        pivotpoint = partition(arr, left, right)
        quicksort(arr, left, pivotpoint)
        quicksort(arr, pivotpoint+1, right)

def partition(arr,left,right) :

    if arr == []:
        return
    pivot = arr[left]
    j = left
    endIndex = len(arr)
    for i in range(left+1,right):
        if(arr[i] < pivot):
            j += 1
            swap(arr,i,j)

    swap(arr,left,j)

    return j


def swap(arr, i, j):
    tmp = arr[i]
    arr[i] = arr[j]
    arr[j] = tmp


arr = [3,4,8,2,1,0]
quicksort(arr, 0, len(arr))
print arr