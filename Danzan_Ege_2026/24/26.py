import re
s = open(r'C:\Users\Zarif\Downloads\1089_1 (1).txt').readline()
m = re.finditer(r'(?=((?:[^Y.]*\.?){5}[^Y.]+))', s)
mx = 0
for x in m:
    mx = max(mx, len(x.group(1)))
print(mx)