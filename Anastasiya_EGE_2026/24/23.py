import string
s = open(r'C:\Users\Zarif\Downloads\196_1 (12).txt').readline()
ct = 0
mx = []
for x in range(len(s) - 1):
    if s[x] != s[x + 1]:
        ct += 1
    else:
        mx.append(ct)
        ct = 0
print(max(mx) + 1)
print(s)
# for x in string.ascii_uppercase:
#     s = s.replace(x + x, x + ' ' + x)
# s = s.split()
# print(s)
# print(len(max(s, key=len)))
# print(max(s, key=len))