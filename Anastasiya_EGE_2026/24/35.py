import re
s = open(r'C:\Users\Zarif\Downloads\1414_1 (3).txt').readline()
m = re.finditer(r'(?=((?:[^T]*T){100}[^T]*))', s)
mx = []
for x in m:
    mx.append(len(x.group(1)))
print(max(mx))