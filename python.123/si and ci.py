p = float(input("enter principle"))
r = float(input("enter rate"))
t = float(input("enter time"))
s = (p*r*t)/100
c = p*(pow((1+r/100),t))
print(c)
print(s)



