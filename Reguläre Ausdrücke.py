
import re
a="8"
if re.match(r'^[1-9]$',a):
    print("a is ok")
else:
    print("a is not")

b="S"
if re.match(r'[g-z]',b):
    print("b is ok")
else:
    print("b is not ok ")



