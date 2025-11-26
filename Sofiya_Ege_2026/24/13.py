import re
s = open(r'C:\Users\Zarif\Downloads\1126_1 (7).txt').readline()
m = re.findall(r'(?:(?:[1-5][0-5]*|0)[+*])+(?:[1-5][0-5]*|0)', s)
print(len(max(m, key=len)))