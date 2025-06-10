import re
s = open(r'C:\Users\Zarif\Desktop\demo_2025_24.txt').readline()
m = re.findall(r'(?:(?:[6-9][06-9]*|0)[-*])+(?:[6-9][06-9]*|0)', s)
print(max(m, key=len))
print(len(max(m, key=len)))