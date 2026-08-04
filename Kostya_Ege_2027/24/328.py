#‪
import re
s = open(r'C:\Users\Zarif\Downloads\328_1 (7).txt').readline()
s = s.replace('CD', '#')
m = re.findall(r'(?=((?:[^#]*#){50}[^#]*))',s)
print(len(max(m, key=len)) + 50 + 2)
print(max(m, key=len))
print(s)