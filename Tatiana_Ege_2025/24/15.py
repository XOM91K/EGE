import re
s = open(r'C:\Users\Zarif\Downloads\1124_1.txt').readline()
m = re.findall(r'(?:(?:[1-9]\d*[05]|0)[+*])+(?:[1-9]\d*[05]|0)', s)
print(len(max(m, key=len)))