import re
s=open('1862_1.txt').readline()
m = re.findall(r'(?=((?:[^A-F]*[A-F]){3}[^A-F]*))', s)
mn_ln = []
for x in m: 
    ct = 0
    for y in '0123456789':
        if y in x:
            ct += 1
    if ct == 10:
        mn_ln.append(x)
print(min(mn_ln, key=len))
print(len(min(mn_ln, key=len)))
# readlinem=10**10
# for p in 'BCDEF':
#     s=s.replace(p,'A')
# c=''
# for r in range(len(s)):
#     c+=s[r]
#     while '1' in c and '2' in c and '3' in c and '4' in  c and '0' in c and '5' in c and '6' in c and '7' in c and '8' in c and '9' in c and c.count('A')==3:
#         m=min(m,len(c))
#         c=c[1:]
#     print(c)
# print(m)