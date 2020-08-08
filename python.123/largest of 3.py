a = int(input("enter 1St no."))
b = int(input("enter 2nd no."))
c = int(input("enter 3rd no."))
if(a>=b) & (a>=c):
    print(a, "is largest")
elif(b>=a) & (b>=c):
    print(b,"is largest")
else:
    print(c, "is largest")
        
