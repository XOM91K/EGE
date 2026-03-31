
import re
t=open(r'C:\Users\Zarif\Downloads\1415_1 (5).txt').readline()
s = t.split('Y')
for x in s:
    if x.count('X') >= 500:
        s = x
print(s.count('X'), len(s) - 2 - 5)
print(s)
# s = s.split('X')
# for x in range(len(s)-499):
#         ln=0
#         s2=''
#         for a in range(500):
#                 ln+=len(s[x+a])
#                 s2+=s[x+a]+'X'
#         mx.append(ln)
#         mx2.append(s2)
# print(min(mx)+500)