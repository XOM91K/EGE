import re
s = open(r'C:\Users\Zarif\Downloads\1125_1 (5).txt').readline()
m = re.findall(r'\w+@\w+\.\w+', s)
print(len(max(m, key=len)))