'''
def operation(a,b):
    sum = a+b
    sub  = a-b
    mul = a*b
    div = a/b
    return [sum,mul,sub,div]
n1= int(input("enter number"))
n2= int(input("enter number"))
print(operation(n1,n2))
'''


'''
def sq(x,y):
 d = x*x+y*y+2*x*y
 return(d)
n1= int(input("enter number"))
n2= int(input("enter number"))
print(sq(n1,n2))
'''


def evenodd(x):
    if(x%2==0):
        print("even")
    else:                                    
        print("odd")
     
n1= int(input("enter number"))
print(evenodd(n1))

'''
def swap(a,b):
    a,b = b,a
    return(a,b)
n1= int(input("enter number"))
n2= int(input("enter number"))
print(swap(n1,n2))


def reverse(a):
    b = a%10
    a = a//10
    return(b,a)
n1= int(input("enter number"))
print(reverse(n1))
'''


