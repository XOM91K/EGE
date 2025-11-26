import re
s = open(r'C:\Users\Zarif\Downloads\826_1 (5).txt').readline()
m = re.findall(r'A(?:[1-6]+[-*])+[1-6]+', s)
print(len(max(m, key=len)))