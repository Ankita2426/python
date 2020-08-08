x = [1,2,3]
try:
    print(x)
except:
    print("none")
'''
try:
     print("hello")
except:
    print("hey")
else:
    print("heyaa")

    
try:
    a = open("abc.txt","r")
except FileNotFoundError:
    s = "FIle is absent"
else:
    s = a.read()
finally:
    print(s)

try:
    print(c)
except:
    print("something went wrong")
else:
    print("no worries")
finally:
    print("everything is finished")

try:
    a = open("abcde.txt","r")
except:
    s = "file is not there"
else:
    s = a.read()
finally:
    print(s)

x = 2
if x<0:
    raise Exception("i m extremly sorry")

'''







































