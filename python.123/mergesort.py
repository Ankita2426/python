def mergesort(a):
    print("splitting",a)
    n = len(a)
    if n>1:
        m = n//2
        l = a[:m]
        r = a[m:]
        mergesort(l)
        mergesort(r)
        i = j = k = 0
        while i<len(l) and j<len(r):
            if l[i]<r[j]:
                a[k] = l[i]
                i = i+1
            else:
                a[k] = r[j]
                j = j+1
            k = k+1
        while i<len(l):
            a[k] = l[i]
            i = i+1
            k = k+1
        while j< len(r):
            a[k] = r[j]
            j = j+1
            k = k+1
    print("merging",a)
a = [2,34,6,54,7,98,0,2,45,7]
mergesort(a)
print(a)
