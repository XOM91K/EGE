import re
s = open(r'C:\Users\Zarif\Downloads\1127_1 (7).txt').readline()
m = re.findall(r'AFD(?:(?:[1-9ABCDEF]\w*|0)[+*])+(?:[1-9ABCDEF]\w*|0)', s)
print(len(max(m, key=len)))
#5+5*13213+123123321*123+05