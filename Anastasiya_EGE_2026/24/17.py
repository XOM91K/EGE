import re
s=open(r'C:\Users\Zarif\Downloads\390_1 (7).txt').readline()
m=re.findall(r'(?:[AEUOYI][^AEUOYI])+[AEUOYI]?|(?:[^AEUOYI][AEUOYI])+[^AEUOYI]?', s)
print(len(max(m, key=len)))
print(max(m, key=len))