import re
s = open(r'C:\Users\Zarif\Desktop\24.txt').readline()
m = re.findall(r'A((?:\d+[+-])+\d+)', s)
d = len(max(m, key=len))
mx = 0
for x in m:
    if len(x) == d:
        print(eval(x))