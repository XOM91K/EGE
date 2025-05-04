import re
s = open(r'C:\Users\Zarif\Downloads\1127_1 (3).txt').readline()
m = re.findall(r'AFD(?:(?:[1-9][0-9]*|0)[+*])+(?:[1-9][0-9]*|0)', s)
#                          (?:(?:[1-5][0-5]*|0)[+*])+(?:[1-5][0-5]*|0)
print(max(m, key=len))
print(len(max(m, key=len)))