import re
s = open(r'C:\Users\Zarif\Downloads\390_1 (4).txt').readline()
m = re.findall(r'[^UEAIOY]?(?:[UEAIOY][^UEAIOY])+', s)
print(len(max(m, key=len)))