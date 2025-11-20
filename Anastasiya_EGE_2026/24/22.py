import re
m=open(r'C:\Users\Zarif\Downloads\340_1 (10).txt').readline()
s=re.findall(r'(?:[^AEUOIY][AEUOIY])+[^AEUOIY]?|(?:[AEUOIY][^AEUOIY])+[AEUOIY]?',m)
print(s)
print(len(max(s,key=len)))