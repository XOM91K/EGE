import re
s = open(r'C:\Users\Zarif\Downloads\1090_1 (7).txt').readline()
m = re.findall(r'(?=((?:[^.]*\.){5}[^.]*))', s)
print(len(max(m, key=len)))