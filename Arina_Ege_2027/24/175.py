import re
s = open('/Users/zarif/Downloads/175_1.txt').readline()
m = re.findall(r'(?:O(?:[^F]*F){0,2}[^F]*)+O', s)
print(len(max(m, key=len)))