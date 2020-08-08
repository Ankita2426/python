'''
d = {"name":"ankita","roll_no":237,"subject":"python"}

print(d)
print(d["roll_no"])

d["subject"]="c++"
print(d)


d["city"] = "yol"
print(d)


d.clear()

if "name" in d:
    del(d["name"]) #in place of name ,ankita won't be there coz it is based on key
    print(d)


d.pop("name")
print(d)


d.pop("subject",0)
print(d)

d.get("roll_no",12)
print(d)

a = d.values()
print(a)

a = d.keys()
print(a)

a = list(d.keys())
print(a)

a = list(d.values())
print(a)


a = d.items()
print(a)


sq = {1:1,3:9,5:25, 2:3}
print(len(sq))
print(sorted(sq))
'''

# ques= make a distionary 0f student

d = {"name": "abc", "class": 12,"roll_no": 235,"subject":"maths","marks":46}

print(d)

a = d.items()
print(a)

a = d.keys()
print(a)

b = d.values()
print(b)


a =  d.get("name")
print(a)

e = d.pop("class")
print(e)

l = len(d)
print(l)

r = d.pop("class",0)
print(r)

d.clear()
print(d)

f = list(d.keys())
print(f)

v  = list(d.values())
print(v)


























































