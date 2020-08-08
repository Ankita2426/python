try:
    a = open("abc.txt","r")
except FileNotFoundError:
    s = "FIle is absent"
else:
    s = a.read()
finally:
    print(s)
