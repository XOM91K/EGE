import re
s = open(r'C:\Users\Zarif\Downloads\24_23381 (2).txt').readline()
m = re.findall(r'[02468]([A-Z]+)[02468]', s)
mx = []
for x in m:
    if len(set(x)) == 1:
        mx.append(len(x))
print(max(mx) + 2)