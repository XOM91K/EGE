import re
s = open('3.txt').readline()
m = re.findall(r'(?:XYZ)+X', s)
print(len(max(m, key=len)))