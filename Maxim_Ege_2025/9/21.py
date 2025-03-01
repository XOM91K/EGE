import re
s = open(r'C:\Users\Zarif\Downloads\1172_1 (2).txt').readline()

m = re.findall(r'(?:(?:[1-9]\d*|0)[+*])+(?:[1-9]\d*|0)', s)
print(max(m, key=len))
mx = max(m, key=len).replace('*', '+').split('+')
mx2 = len(mx)
print(mx2)
