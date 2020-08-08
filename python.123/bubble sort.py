def bubblesort(a):
    n = len(a)
    for t in range(n-1,0,-1):
        for i in range(t):
            if a[i]>a[i+1]:
                a[i],a[i+1]= a[i+1],a[i]
a = [22,3,5,78,6,1,0,98,65]
bubblesort(a)
print(a)
