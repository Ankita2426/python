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