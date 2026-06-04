import re
s = open(r'C:\Users\Zarif\Downloads\1862_1.txt').readline()
m = re.findall(r'(?=((?:[^A-F]*[A-F]){3}[^A-F]*))', s)
mn_ln = []
for x in m:
    for y in '0123456789':
        if y not in x:
            break
    else:
        print(x)
        mn_ln.append(x)
print(min(mn_ln, key=len))
print(len(min(mn_ln, key=len)))