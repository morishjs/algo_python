#mergesort
list = [3,2,5,6,7,1,13,0]

def mergesort(lst):
    if len(lst) == 1:
        return lst
    else :
        half = len(lst)/2
        left = mergesort(lst[0:half])
        right = mergesort(lst[half:])

        mi = min(len(left), len(right))
        mx = max(len(left), len(right))
        b = []
        i = 0
        j = 0
        while(i < mi and j < mi):
            if left[i] > right[j]:
                b.append(right[j])
                j += 1
            else :
                b.append(left[i])
                i += 1
        if i > j:
            b += right[j:mx]
        elif i < j:
            b += left[i:mx]
        return b


print mergesort(list)



