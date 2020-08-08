n = int(input("enter a number: "))
i=2
while i<n:
    if(n%i==0):
        print("not prime")
        i=i+1  #for next values of i
    else:    
        print("prime")
    break  #for termination of loop ,break is used
