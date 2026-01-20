import re
s = open(r'C:\Users\Zarif\Downloads\403_1 (8).txt').readline()
for x in range(5):
    s = s.replace('XXXX', 'XX XX')
    s = s.replace('YYYY', 'YY YY')
    s = s.replace('ZZZZ', 'ZZ ZZ')

s = s.split(' ')
mx = []
for x in s:
    ct = 0
    for y in range(0, len(x) - 1, 2):
        if x[y] == x[y + 1]:
            ct += 2
        else:
            mx.append(ct)
            ct =0
print(max(mx))
print(s)
# ln = 0
# mx = []
# print(s)
# dd = s[7922:7982]
# for x in range(len(s) - 1):
#     #
#     if x == 7922:
#         print('ok')
#     if s[x] == s[x + 1] and s[x] in '#@$':
#         mx.append(ln)
#         ln = 0
#     elif s[x] != s[x + 1] and s[x] in '#@$':
#         ln += 2
#     elif (s[x] not in '#@$' or s[x + 1] not in '#@$') or (s[x] in '#$@' and s[x + 1] not in '#$@') or (s[x] not in '#$@' and s[x + 1]  in '#$@') :
#         ln += 1
#
# # X#
# print(max(mx))