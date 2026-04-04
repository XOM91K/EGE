import re
s = open(r'C:\Users\Zarif\Downloads\1483_1 (12).txt').readline()
s = s.replace('CDE', '@')
m = re.findall(r'(?=((?:@\w*){86}@E*[^E]+?))', s)
print(len(min(m, key=len)) + 87 * 2)