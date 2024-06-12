import string
for x in string.ascii_uppercase:
    print(x)
import re
s = open(r'C:\Users\Zarif\Downloads\24_633_1 (2).txt').readline()
m = re.findall(r'(?:[BCDFGHJKLMNPQRSTVWXZ][A-Z][AEIOUY])*', s)
print(max(m, key=len))