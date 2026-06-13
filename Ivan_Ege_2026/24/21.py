import re
s = open(r'C:\Users\Zarif\Downloads\24 (33).txt').readline()
a = re.findall(r'(?=([0-9]+))', s)
mx = []
for e in a:
    if len(set(str(e))) <= 3:
        mx.append(e)
print(len(max(mx, key=len)))
print(max(mx, key=len))