import re
s = open(r'C:\Users\Zarif\Downloads\24_612_1.txt').readline()
m = re.findall(r"(?:AB)+A?", s)
print(max(m, key=len), len(max(m, key=len)))
print(s)
