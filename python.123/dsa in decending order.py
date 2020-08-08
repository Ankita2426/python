
def bubblesort(a):
    n = len(a)
    for i in range(n-1,0,-1):
        for j in range(i):
            if a[j]<a[j+1]:
                a[j],a[j+1]=a[j+1],a[j]
a = [1,56,7,4,0,98,7]
bubblesort(a)
print(a)

def insertionsort(a):
    n = len(a)
    for i in range(1,n):
        t = a[i]
        j = i-1
        while j>=0 and t>a[j]:
            a[j+1]=a[j]
            j = j-1
        a[j+1] = t
a = [23,4,56,7,0,2,10,1]
insertionsort(a)
print(a)


