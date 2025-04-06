import re
s = open(r'C:\Users\Zarif\Downloads\24_21161.txt').readline()
m = re.findall(r'[A-C][a-c]* (?:[A-C]?[a-c]+ )*[A-C]?[a-c]+\.', s)
print(len(max(m, key=len)))
print(max(m, key=len))