import re
s = open(r'C:\Users\Zarif\Downloads\1124_1 (6).txt').readline()
m = re.findall(r'(?:(?:[1-9][0-9]*)?[05][+*])+(?:[1-9][0-9]*)?[05]', s)
print(max(m, key=eval))
print(len(max(m, key=len)))