
a = [2,3,4,5,6]
b = [1,3,5,7,8]
for x in zip(a,b):
    print(x)

x = ['a','b','s','f']                    #zip
y = ['t','r','u','f']
for a in zip(x,y):
    print(a)


a = ['a','d','g','r','h']
b = [1,4,5,7,8]
for c in zip(a,b):
    print(c)


def sum(a,b):
    return(a+b)
x = [1,2,3]
y = [4,5,6]                          #map
l = [x for x in map(sum,x,y)]
print(l)

def even(a):
    if(a%2==0): return True
    else: return False         #filter
        
a = [1,2,3,4,5,6,7,8,9]
l = [x for x in filter(even,a)]
print(l)


def odd(a):
    if(a%2==1): return True
    else: return False
a = [1,2,3,4,5,6,7,8,9]
l = [x for x in filter(odd,a)]
print(l)

sq = lambda x:x*x
a = lambda x:x*x*x*x*x*x*x*x*x*x        #lambda
print(sq(5))
print(a(2))


x = [2,3,4,5]
y = [1,2,3,4]
l = [x for x in map(lambda a,b:a+b,x,y)]
print(l)















































