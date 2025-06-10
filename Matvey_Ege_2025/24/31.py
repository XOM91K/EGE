import re
s = open(r'C:\Users\Zarif\Downloads\1172_1 (5).txt').readline()
m = re.findall(r'(?:[1-9][0-9]*[+*])+[1-9][0-9]*', s)

s = max(m, key=lambda d: d.count('+') + d.count('*'))
print(s.count('+') + s.count('*') + 1)


