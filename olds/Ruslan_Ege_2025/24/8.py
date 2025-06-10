import string
s = open(r'C:\Users\Zarif\Downloads\196_1 (3).txt').readline()
mx_ln = 0
ct = 1
print(s)
for x in range(len(s) - 1):
    if s[x] != s[x + 1]:
        ct += 1
    else:
        mx_ln = max(mx_ln, ct)
        ct = 1
print(mx_ln)
# for x in string.ascii_uppercase:
#     s = s.replace(x + x, '#')
# s = s.split('#')
# print(len(max(s, key=len)) + 2)
