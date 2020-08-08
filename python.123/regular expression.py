'''
import re
a = "my name is ankita"

x = re.search("name",a)
print(x)
if(x):                                 #to find weather this letter or word exist in a or not
    print("yes we have a match")
else:
    print("no match")
'''
'''

import re
a = "my name an  is ankita"             #to list this word or letter 

x = re.findall("an",a)
print(x)


import re
a = "m n i a"               
x = re.split("\s",a)
print(x)
'''
'''
import re
a = "my name is ankita"
x = re.sub("\s","9",a)
print(x)
'''

import re
a = "oo chachu all is well"
x = re.compile(a)
print(x)

