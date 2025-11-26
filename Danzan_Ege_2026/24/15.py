import re
s = open(r'C:\Users\Zarif\Downloads\826_1 (4).txt').readline()
m = re.findall(r'A(?:\d+[-*])+\d+', s)
print(len(max(m, key=len)))
print((max(m, key=len)))