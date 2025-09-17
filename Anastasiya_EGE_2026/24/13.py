# dz 1
import re
s = open(r'C:\Users\Zarif\Downloads\24_318 (2).txt').readline()
m = re.findall(r'\d+[13579]', s)
print(max(m, key=int))