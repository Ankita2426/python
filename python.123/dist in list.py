d = {"name":"abc","marks":[20,30,45],"subject":["english","maths","python"]}
'''
print(d)
a = len(d["marks"])
print(a)

b = d["marks"][1]
print(b)


c = d.keys()
print(c)

d = d.get("marks")     #get me add keys
print(d)


e = d.pop("subject")
print(e)


f = d.copy()
print(f)
'''
