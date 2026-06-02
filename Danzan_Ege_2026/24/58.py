#‪
import re
s = open(r'C:\Users\Zarif\Downloads\175_1 (16).txt').readline()
m = re.findall(r'(?:O(?:[^OF]*F){,2}[^OF]*)+O', s)
print(len(max(m, key=len)), max(m, key=len))