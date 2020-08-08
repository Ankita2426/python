a = input("enter string")
n = len(a)
for i in range(0,n):
    for j in range(0,i+1):
        print(a[j],end="")
    print()
