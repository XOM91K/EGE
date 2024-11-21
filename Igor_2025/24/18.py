s = open('18.txt').readline()
sp = ''
mx = 0
for x in range(len(s)):
    if s[x] not in sp:
        sp += s[x]
    else:
        mx = max(mx, len(sp))
        sp = sp[sp.index(s[x]) + 1:] + s[x]

print(mx)
# for x in range(len(s) - 1):
#     if s[x] != s[x + 1]:
#         ct += 1
#     else:
#         mx = max(mx, ct)
#         ct = 1