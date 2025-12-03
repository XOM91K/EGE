import re
s = open(r'C:\Users\Zarif\Downloads\1414_1 (2).txt').readline()
m = re.finditer(r'(?=((?:[^T]*T){100}[^T]*))', s)
mx = 0
for x in m:
    mx = max(mx, len(x.group(1)))
print(mx)