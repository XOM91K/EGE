import re
s = open(r'C:\Users\Zarif\Downloads\24_608_1 (3).txt').readline()
m = re.findall(r"X+", s)
print(len(max(m, key=len)))