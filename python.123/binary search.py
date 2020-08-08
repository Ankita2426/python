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
