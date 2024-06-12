import re
s = open(r'C:\Users\Zarif\Downloads\24_629_1 (1).txt').readline()
m = re.findall(r"(?:[A-Z]*\.){3}[A-Z]+", s)
print(len(max(m, key=len)))
