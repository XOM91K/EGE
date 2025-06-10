import re
s = open(r'C:\Users\Zarif\Desktop\demo_2025_24.txt').readline()
m = re.findall(r'(?:(?:[1-9]\d*|0)[-*])+(?:[1-9]\d*|0)', s)
print(len(max(m, key=len)))