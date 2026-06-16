# ‪C:\Users\Zarif\Downloads\24 (39).txt
import re, itertools
s = open(r'C:\Users\Zarif\Downloads\24 (39).txt').readline()
# m = re.findall(r'\d+', s)
mxln=[]
for x in itertools.combinations('0123456789', 3):
    x = ''.join(x)
    #print(x)
    m = re.findall(rf'[{x}]+', s)
    mxln.append(len(max(m, key=len)))
print(max(mxln))