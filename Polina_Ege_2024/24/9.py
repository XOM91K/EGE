import re
s = open('24_demo (3).txt').readline()
m = re.findall(r"(?:XYZ)+(?:X|XY)?", s)
print(max(m, key=len))