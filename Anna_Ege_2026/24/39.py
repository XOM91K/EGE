import re
s = open(r'C:\Users\Zarif\Downloads\1862_1 (1).txt').readline()
m = re.findall(r'(?=((?:[^ABCDEF]*[A-F]){3}[^ABCDEF]*))', s)
mn_ln = []
for x in m:
    ct = 0
    for y in '0123456789':
        if y in x:
            ct += 1
    if ct == 10:
        mn_ln.append(x)
print(len(min(mn_ln, key=len)), min(mn_ln, key=len))