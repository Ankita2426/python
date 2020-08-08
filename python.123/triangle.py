n = int(input("enter number"))
i = 1#initialize krne ke liye
k = 2*n-2
for i in range(0,n):
    for j in range(0,k):
        print(end=" ")
    k= k-1
    for j in range(0,i+1): #bahr vali loop ke andr kaam karegi
        print("* ",end="") #ek line me assign krne ke liye end keyword use hoga
    print("\r") #line terminate ho gyi h,next iski help se hogi
