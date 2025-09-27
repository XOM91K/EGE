import re
l = open(r'C:\Users\Zarif\Downloads\327_1 (4).txt').readline()
m = re.findall(r'[A-Z]([1-9]\d+[24680])[A-Z]',l)
print(max(m, key=int), m)