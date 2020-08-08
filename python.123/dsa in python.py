'''
def bubblesort(a):
    n = len(a)
    for t in range(n-1,0,-1):
        for i in range(t):
            if a[i]>a[i+1]:
                a[i],a[i+1]= a[i+1],a[i]
a = [22,3,5,78,6,1,0,98,65]
bubblesort(a)
print(a)


def insertionsort(arr):
    for i in range(1,len(arr)):
        a = arr[i]
        j = i-1
        while j>=0 and a <arr[j]:
            arr[j+1]=arr[j]
            j = j-1
        arr[j+1]= a
arr = [23,4,54,67,3,5,6]
insertionsort(arr)
print(arr)

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

def quicksort(a):
    n = len(a)
    c(a,0,n-1)   
def c(a,f,l):   # f = first element , l = last element
    if f<l:
        s = p(a,f,l)   #s = splitpoint , p = partion
        c(a,f,s-1)
        c(a,s+1,l)
def p(a,f,l):
    P = a[f]      # P = pivot value
    L = f+1      # L = left mark
    R = l          # R = rightmark
    done =  False
    while not done:
        while L<=R and a[L]<= P:
            L = L+1
        while  a[R]>= P and  R>=L:
            R = R-1
        if R<L:
            done = True
        else:
          a[L],a[R] = a[R],a[L]
    a[f],a[R] = a[R],a[f]
    return R
a= [23,43,56,7,1,0,87,9,8,47]
quicksort(a)
print(a)

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

import heapq
def heapsort(h):
    heap = []
    for value in h:
        heapq.heappush(heap,value)
    return [heapq.heappop(heap) for i in range(len(heap))]
print(heapsort([12,3,5,6,0,1]))

def sequential_search(a,item):
    n = len(a)
    p = 0      #p = position
    found =  False
    while p<n and not found:
        if a[p] == item:
            found = True
        else:
            p = p+1
    return found,p
print(sequential_search([11,23,5,7,98,10,0,34,65],234))


def binary_search(a,item):
    n = len(a)
    f = 0
    l = n-1
    found = False
    while (f<=l and not found):
        m = (f+l)//2
        if a[m] == item:
            found = True
        else:
            if item<a[m]:
                l = m-1
            else:
                f = m+1
    return found
print(binary_search([2,3,4,56,7],5))
print(binary_search([2,3,4,56,7],4))
'''
import math
a = [2,3]
b = [6,4]
d = math.sqrt(((a[0]-b[0])**2)+((a[1]-b[1])**2))
print(d)


                
