a = int(input("enter range"))
k = 2*a-2
for i in range(0,a):
    for j in range(0,k):
        print(end=" ")
    k = k-1
    for j in range(0,i+1):
        print("a ",end="")
    print("\r")
