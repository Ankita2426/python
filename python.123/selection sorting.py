def selectionsort(a):
    n = len(a)
    for c in range(n-1,0,-1):
        m = 0
        for i in range(1,c+1):
            if a[i]>a[m]:
                m = i
        a[c],a[m] = a[m],a[c]
a = [34,5,2,0,7,5,89,76]
selectionsort(a)
print(a)
                
