# import string
# print(string.ascii_uppercase)
# import re
# s = open('3.txt').readline()
# m = re.findall('[ABCDEFGHIJKLMNOPQRSTUVWZ]+X[ABCDEFGHIJKLMNOPQRSTUVWZ]+Y[ABCDEFGHIJKLMNOPQRSTUVWZ]+|[ABCDEFGHIJKLMNOPQRSTUVWZ]+Y[ABCDEFGHIJKLMNOPQRSTUVWZ]+X[ABCDEFGHIJKLMNOPQRSTUVWZ]+', s)
# print(max(m, key=len), len(max(m, key=len)))
s = open('3.txt').readline()
d = ''
ct = 0
print(s)
mx = 0
for x in range(len(s)):
    ct += 1
    if s[x] in 'XY':
        d += s[x]
        if len(d) == 3 and len(set(d[:-1])) == 2:
            mx = max(mx, ct)
            ct = 0
            d = d[-1]
        elif len(set(d[:-1])) != 2:
            d = d[-1]
print(mx)