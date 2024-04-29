import re
s = open(r'C:\Users\Zarif\Downloads\24_12254.txt').readline()
m = re.findall(r"[RSQ]{3}(?:RSQ)+[RSQ]{3}", s)
print(max(m, key=len))