a = input("enter string")
length = len(a)
for row in range(0,length):
    for col in range(0,row+1):
        print(a[col],end="")
    print()
