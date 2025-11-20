import re
s = open(r'C:\Users\Zarif\Downloads\175_1 (14).txt').readline()
m = re.findall(r'(?:O(?:[^FO]*F){,2}[^FO]*)+O', s)
print(len(max(m, key=len)))