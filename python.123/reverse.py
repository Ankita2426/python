n = int(input("enter number"))
i = n#initialize krne ke liye
k = 2*n-2 #star ko left side trim krne ke liye we use this logic
for i in range(0,n):
    for j in range(0,k):
        print(end=" ")
    k= k-2 #to give positioning to star
    for j in range(0,i+1): #bahr vali loop ke andr kaam karegi
        print("* ",end="") #ek line me assign krne ke liye end keyword use hoga
    print("\r") #line terminate ho gyi h,next iski help se hogi
