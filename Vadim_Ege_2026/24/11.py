import re
s = open(r'C:\Users\Zarif\Downloads\1125_1 (8).txt').readline()
m = re.findall(r'\w+@\w+\.\w+', s)
print(max(m, key=len))
print(len(max(m, key=len)))
