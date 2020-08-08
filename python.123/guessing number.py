import random
x = random.randint(1,5)
a = int(input("enter number"))
for a in range(1,5):
    if(x==a):
        print("true")
    else:
        print("false")
    break
print(x)
