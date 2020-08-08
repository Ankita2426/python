
class variable:
    x = 10
    y = 15
    s = x+y
    print(s)

t = variable()
print(t.x)


class person:
    def __init__(self,name,age):      #this is construct (default) ie a function that is called at the time of initiation
        self.name = name
        self.age = age
x = person("ankita",18)
print(x.name)
print(x.age)

class person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def myfunc(self):
        print("name is "+ self.name)
x = person("anki",18)
x.myfunc()

x.age = 20
print(x.age)
del x.age


class point:
    pass
    
p = point()
p.x = 10
p.y = 20
print(p.x,p.y)


class point:
    def __init__(c,a,b):   # this is initiation
        c.x = a       #here values are assigned to variable
        c.y = b
p = point(10,234)    # here values are assigned
print(p.x,p.y)

# values can be assigned in initialization process as a = 0,b = 0

#  adding a metthod
class point:
    def __init__(self,a=0,b=0):
        self.x = a
        self.y = b
        
    def display(self):
        print(self.x,self.y)
p = point(2,3)   #to call the values it is under class
p.display()

class example:
    def __init__(a):
        print("object created")
    def __del__(a):
        print("object destroyed")
myobj = example()
del myobj

    







    























































