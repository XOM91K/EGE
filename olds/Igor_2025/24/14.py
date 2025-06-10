import re
s = open('14.txt').readline()
m = re.findall(r'(?:(?:[6-9]+[06-9]*|0)[-*])+(?:[6-9]+[06-9]*|0)', s)
print(max(m, key=len))