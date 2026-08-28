import re
s = open(r'C:\Users\Zarif\Downloads\1397_2 (17).txt').readline()
s = s.replace('RSQ', '#')
m = re.findall(r'(?=((?:#\w*){129}#Q*[^Q]))', s)
print(len(min(m, key=len)) + 2 * 130)