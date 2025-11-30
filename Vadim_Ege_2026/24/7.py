import re
l = open(r"C:\Users\Zarif\Downloads\340_1 (14).txt").readline()
m = re.findall(r'[^AEOIUY]?(?:[AEOIUY][^AEOIUY])+[AEOIUY]?',l)
print(len(max(m,key=len)))