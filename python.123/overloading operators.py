'''
class A:
    def __init__(self,a):
        self.a = a
    def __add__(self,o):
        self.o = o                          #addition of numbers and concartination of strings
        return self.a+o.a
ob1 = A(1)
ob2 = A(3)
ob3 = A("hey ")
ob4 = A("hello")
print(ob1+ob2)
print(ob3+ob4)

class A:
    def __init__(self,a):
        self.a = a
    def __sub__(self,o):
        self.o = o
        return self.a-o.a
ob1 = A(1)                               #subtraction of numbers
ob2 = A(3)
print(ob1-ob2)
'''
class numbers:
    def __init__(self,a):
        self.a = a
    def __it__(self,b):
        if(self.a<b.a):
            return "t1 is less than t2"
        else:
            return "t2 is less then t1"
    def __eq__(self,b):
        if(self.a == b.a):
            return "both are equal"
t1 = numbers(1)
t2 = numbers(4)
print(1<2)

t3 = numbers(3)
t4 = numbers(4)
print(1==2)



    
    
