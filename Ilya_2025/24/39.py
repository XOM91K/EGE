import re
s = open(r'C:\Users\Zarif\Downloads\1127_1.txt').readline()
m = re.findall(r'AFD(?:(?:[1-9][0-9]*|0)[+*])+(?:[1-9][0-9]*|0)', s)
print(max(m, key=len))
print(len(max(m, key=len)))