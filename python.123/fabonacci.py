num = int(input("enter range"))
i=0
f=0
s= 1
while(i<num):
    if(i <=1):
        n=i
    else:
        n = f+s
        f= s
        s= n
    print(n) #this indentation is under while loop so thar it can execute
    i=i+1
 
        
