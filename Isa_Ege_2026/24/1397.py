import re
s = open(r'C:\Users\Zarif\Downloads\1397_2 (15).txt').readline()
s = s.replace('RSQ', '#')
m = re.findall(r'(?=((?:#[^#]*){129}#Q*[^Q]+?))', s)
print(len(min(m, key=len)) + 130 * 2)