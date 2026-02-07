import string
s = open(r'C:\Users\Zarif\Downloads\24 (29).txt').readline()
for x in string.ascii_uppercase:
    s = s.replace(x + x, x + ' ' + x)
s = s.split()
print(len(max(s, key=len)))
# ct = 1
# mx_ct = 0
# print(s)
# for x in range(len(s) - 1):
#     if s[x] != s[x + 1]:
#         ct += 1
#         mx_ct = max(mx_ct, ct)
#     else:
#         ct = 1
# print(mx_ct)