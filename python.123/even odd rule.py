n = int(input("enter range of numbers"))
y = n
sum = 0
i=1
print('---------------')
while(i<n):
    sum = n%10
    print('---------------')
    n = n/10
    y = sum +y
    print(y)
    i = i+1
    
