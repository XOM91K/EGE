import re
a= open(r'C:\Users\Zarif\Downloads\1124_1 (1).txt').readline()
m = re.findall(r'(?:(?:[1-9]\d*[05]|0)[+*])+(?:[1-9]\d*[05]|0)', a)
print(len(max(m, key=len)))