import re
s = open(r'C:\Users\Zarif\Downloads\24_24895.txt').readline()
m = re.findall(r'(?=(?:\d+[+*]){39}\d+)', s)
mx = 0
for x in m:
    mx = max(mx, x.group(0))
print(mx)
#print(len(max(m, key=len)))