import re
s = open(r'C:\Users\Zarif\Downloads\24_15339 (12).txt').readline()
m = re.findall(r'\d?(?:[A-C]\d)+', s)
print(len(max(m, key=len)))
