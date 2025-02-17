import re
s = open(r'C:\Users\Zarif\Downloads\403_1 (1).txt').readline()
#s = 'ASDASDXXYYZZZZASDASDSDS'
flag = 'W'
x = 0
ln = 0
mx_ln = 0
while x < len(s) - 1:
    if s[x] == s[x + 1] and s[x] in 'XYZ' and s[x + 1] in 'XYZ':
        if flag != s[x]:
            ln += 2
            mx_ln = max(mx_ln, ln)
            flag = s[x]
            x += 1
        else:
            mx_ln = max(mx_ln, ln)
            flag = s[x + 1]
            ln = 0
    if mx_ln == 50:
        print(s[x - 1:x - 1 + 54])
        break
    x += 1

print(mx_ln)
# s = s.replace('YYZZ', '####')
# s = s.replace('XXYY', '####')
# s = s.replace('YYXX', '####')
# s = s.replace('ZZYY', '####')
# s = s.replace('XXZZ', '####')
# s = s.replace('ZZXX', '####')
# print(s)
#m =re.findall(r'XXYYZZ', s)
#s = 'ASDASDXXYYZZZZASDASDSDS'
#s = s.replace('ZZ', '#').replace('XX', '#').replace('YY', '#')
# print(s)
# flag = 'W'
# ln = 1
# mx_ln = 1
# for x in range(len(s) - 1):
#     if s[x] == s[x + 1] and s[x] in 'XYZ':
#         if flag != s[x]:
#             ln += 1
#             mx_ln = max(mx_ln, ln)
#             flag = s[x]
#             x += 1
#         else:
#             mx_ln = max(mx_ln, ln)
#             ln = 1
#     else:
#         ln = 1
# y = []
# for i in range(len(s) - 3):
#     if s[i] == s[i + 1]:
#         if s[i] + s[i + 1] != s[i + 2] + s[i + 3]:
#             c += s[i] + s[i + 1] + s[i + 2] + s[i + 3]
#         else:
#             y.append(c)
#             c = ''
#     else:
#         continue
# print(len(max(y, key=len)))
print(len('############################################'))