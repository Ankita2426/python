a = {1,23,4,56,7,45}
n = max(a)
print(n)




a = [1,34,56,32,78,4]
n = len(a)
for i in n:
    a[0],a[n-1]=a[n-1],a[0]
    print(a[0],a[n-1])
    print(a)
    i = i+1
    
