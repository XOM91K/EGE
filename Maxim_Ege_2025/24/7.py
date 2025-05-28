import re
s = open(r'C:\Users\Zarif\Downloads\1332_1 (1).txt').readline()
m = re.findall(r'(?:(?:[7-9]\d*|0)[-*])+(?:[7-9]\d*|0)', s)
print(len(max(m,key=len)))