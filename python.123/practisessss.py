def bubblesort(a):
    n = len(a)
    for i in range(n-1,0,-1):
        for j in range(i):
            if a[j]<a[j+1]:
                a[j+1],a[j]=a[j],a[j+1]
a = [1,56,7,4,0,98,7]
bubblesort(a)
print(a)
