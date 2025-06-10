# s = open('10.txt').readline()
# ct = 3
# mx = 0
# for i in range(len(s) - 3):
#     st = set(s[i] + s[i + 1] + s[i + 2] + s[i + 3])
#     g = s[i] + s[i + 1] + s[i + 2] + s[i + 3]
#     if not(len(st) == 1 and (st == {'Z'} or st == {'X'} or st == {'Y'})):
#         if (g.count('X') == 2 and g.count('Y') == 2) or (g.count('X') == 2 and g.count('Z') == 2) or (g.count('Y') == 2 and g.count('Z') == 2):
#             print(st)
#             print(s[i] + s[i + 1] + s[i + 2] + s[i + 3])
#             print(ct)
#             ct += 1
#             mx = max(mx, ct)
#     else:
#         ct = 3
# print(mx)
import re

l =  open('10.txt').readline()
m = re.findall('(?:(?:ZZ(?:XX(?:YY|ZZ)|YY(?:ZZ|XX)))|(?:YY(?:XX(?:YY|ZZ)|ZZ(?:YY|XX)))|(?:XX(?:ZZ(?:YY|XX)|YY(?:ZZ|XX))))+', l)
s = []
for i in m:
    can = True
    for n in range(0, len(i) - 3):
        if (i[n]+i[n+1]) == (i[n+2]+i[n+3]):
            can = False
    if can:
        s.append(i)

print(max(s, key=len))