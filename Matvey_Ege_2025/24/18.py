import re
s = open(r'C:\Users\Zarif\Downloads\1124_1 (3).txt').readline()
m = re.findall(r'(?:(?:[1-9]\d*[05]|[05])[+*])+(?:[1-9]\d*[05]|[05])', s)
print(len(max(m, key=len)))