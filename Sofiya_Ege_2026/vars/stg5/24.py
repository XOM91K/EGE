import re
s = open(r'C:\Users\Zarif\Documents\24.txt').readline()
m=re.findall(r'1[A-Z]+1|3[A-Z]+3|5[A-Z]+5|7[A-Z]+7|9[A-Z]+9',s)
mx = []
for x in m:
    ctgl = 0
    ctsg = 0
    for y in x:
        if y in 'AEOIUY':
            ctgl += 1
    ctsg = len(x) - ctgl - 2
    if ctgl == ctsg:
        mx.append(x)
print(max(mx, key=len))
print(len(max(mx, key=len)))