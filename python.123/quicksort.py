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
        