import re
s = open('7.txt').readline()
m = re.findall('E[ACDFO]*?B(?:[ACDFO]*?A){6,100}?[ACDFO]*?B[ACDFO]*?E', s)
print(len(min(m, key=len)))
print(min(m, key=len))
print(m)