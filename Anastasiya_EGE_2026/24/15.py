#dz3
import re
s = open(r'C:\Users\Zarif\Downloads\24_2420.txt').readline()
m = re.findall(r'[ABEF]+', s)
print(len(max(m, key=len)))