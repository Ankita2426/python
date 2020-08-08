n = int(input("enter number"))
sum  = 0
temp = n121
while(temp>0):
    b = temp%10
    sum = sum + (b**3)
    temp = temp//10
if(n == sum):
    print("armstrong")
else:
    print("not armstrong")
