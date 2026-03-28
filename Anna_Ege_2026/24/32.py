import re
s = open(r'C:\Users\Zarif\Downloads\1062_1 (11).txt').readline()
s = s.replace('FGSW', '#')
m = re.findall(r'(?=((?:[^#]*#){85}[^#]*))', s)
print(len(max(m, key=len)) + 3 * 85)