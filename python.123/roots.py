from math import sqrt
a = int(input("enter 1st number"))
b = int(input("enter 2nd number"))
c=  int(input("enter 3rd number"))
d = (b**2)-(4*a*c)
if(d>0):
    x1 = (-b+sqrt(d))/(2*a)
    x2 = (-b-sqrt(d))/(2*a)
    print(x1,x2)
elif(d==0):
    x = (-b)/2*a
    print(x)
else:
    print("nothing")
