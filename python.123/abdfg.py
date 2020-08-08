d = {"name":"ankita","roll_no.":237,"marks":[12,34,56],"subject":["maths","python","c++"]}
print(d)

a = len(d["marks"])
print(a)

b = d["marks"][1]
print(b)


c = d.keys()
print(c)

d = d.get("marks")     #get me add keys
print(d)


f = d.copy()
print(f)


