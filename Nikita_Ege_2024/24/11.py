import re
s = open(r'C:\Users\Zarif\Downloads\24_10724.txt').readline()
m = re.findall(r'[1-9A-F][0-9A-F]+', s)
print(len(max(m, key=len)))
print(m)