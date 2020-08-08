'''
x = abs(-12.3)
print(x)

my_list = [True,False,True]
x = all(my_list)
c = any(my_list)
print(x)
print(c)

x = ord('a')
print(x)

x = bin(234)
c = bool(0)
print(x)
print(c)

x = bytearray(25)
c = bytes(234)
print(x)
print(c)

def x():
    a = 10
print(callable(x))

x = chr(97)
print(x)

x = compile('print(55)','ankita','absdffg')
exec(x)
print(x)                    #have to be done in anaconda

x= complex(2,4)
print(x)

class person:
    name = "ankita"
    age = 18
    city = "yol"                         #why output window is blank?
x = delattr(person,"age")
y = dir(person)
z = getattr(person,'city')
t = hasattr(person,"city")
print(t)
print(x)
print(y)
print(z)


x = dict(key="value",ankita="good girl")
print(x)

x = divmod(5,2)
print(x)

x = ('apple','banana','cherry')
y = enumerate(x)
z = frozenset(x)
t = id(x)
print(t)
print(list(y))
print(z)

x = 'print(55)'
eval(x)

x = 'name = "abcd"\nprint(name)'
exec(x)

def even(x):
    if(x%2 ==0):return True
    else: return False
a = [2,3,4,5,5,6,78,7,2,355]
b = [x for x in filter(even,a)]
print(b)

x = float(34)
print(x)
x = format(2,'%')
print(x)
'''

x = globals()
print(x)

x = hex(255)
print(x)


print("enter your name")
x = input()
print('hello' +x)

x = int(3.45)
print(x)

x = isinstance(2.4,int)          #check weaTHER no. is integer or not
print(x)

class person:
    name = "ankita"
class age(person):
    age = 18
    name = "person"               
x = issubclass(age,person)
print(x)

x = iter(["abc","asd"])
print(next(x))


x = locals()
print(x)


x = max(3,5)
print(x)

x = memoryview('abcdef')
print(x)                                 #doubt.....?
print(x[2])
            
x = min(5,8)
print(x)

x = object()
print(x)


x = oct(34)
print(x)

x = pow(2,5)
print(x)


print("hey")

x = ord('h')
print(x)


x = range(10)
for n in x:
    print(n)

a = ['a','s','d','f','t']
x = reversed(a)
for x in x:
    print(x)

s = round(5.456789,2)
print(s)


x = set(('a','s','d','e'))
print(x)

class person:
    name = "ankita"
    age = 18
setattr(person,'age',23)
x = getattr(person,'age')
print(x)


a = ('a','s','d','f','g','h','j','y','e')
x = slice(3)
y = sorted(a)
print(y)
print(a[x])

a = (1,2,3,4,5,6)
x = sum(a)
print(x)

a = ('','','',)
b = 12345
c = "ankita"
x = type(a)
t = type(b)
y = type(c)
print(x)
print(t)
print(y)

class person:
    name = "ankita"
    age =  18
x = vars(person)
print(x)

a = [1,2,3]
b = [2,4,6]
x = zip(a,b)
print(tuple(x))
'''


































