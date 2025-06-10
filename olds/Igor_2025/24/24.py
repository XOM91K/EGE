import re

s = open(r'C:\Users\Zarif\Desktop\1265_1.txt').readline()
r = re.findall('(?:(?:[789][7890]*|0)[-*])+(?:[789][7890]*|0)', s)

print(max(r, key=len))
print(len(max(r, key=len)))
print(eval(max(r, key=len)))