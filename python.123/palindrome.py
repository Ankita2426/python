a = int(input("enter a number"))
temp = a
b = 0
while(a>0):
   b= b*10 + a%10
   a = a//10
if(b==temp):
    print("palindrome")
else:
    print("not")
   
