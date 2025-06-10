import re
f = open(r'C:\Users\Zarif\Downloads\1124_1 (2).txt').readline()
match = re.findall(r'(?:(?:[1-9]\d*[05]|5|0)[+*])+(?:[1-9]\d*[05]|5|0)?', f)
print(len(max(match, key=len)))
print((max(match, key=len)))