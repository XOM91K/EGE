import re
s = open(r'C:\Users\Zarif\Downloads\1397_2 (7).txt').readline()
s = s.replace('RSQ', '#')
m = re.finditer(r'(?=((?:[^#]*?#){130}[^Q]*?))', s)
mx = []
for x in m:
    mx.append(len(x.group(1)))
print(min(mx))
# Дорешать