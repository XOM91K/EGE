import re
s = open(r'C:\Users\Zarif\Downloads\1697_1.txt').readline()
m = re.findall(r'(?:\([1-9]\d*[02468][+-][1-9]\d*[13579]\))+', s)
print(len(max(m, key = len)))
print(max(m, key = len))