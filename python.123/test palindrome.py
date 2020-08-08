n = int(input("enter numbers"))
rev = 0
temp = n
while(n>0):
    rev = rev*10 + n%10
    n = n//10
if(rev == temp):
    print("palindrome")
else:
    print("not palindrome")
