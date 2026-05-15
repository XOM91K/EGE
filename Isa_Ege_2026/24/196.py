# import re
import string
s = open(r'C:\Users\Zarif\Downloads\196_1 (15).txt').readline()
for x in string.ascii_uppercase: # A B C ...
    s = s.replace(x + x, '#')
s = s.split('#')
print(max(s, key=len))
print(len(max(s, key=len)) + 2)
# m = re.findall(r'', s)