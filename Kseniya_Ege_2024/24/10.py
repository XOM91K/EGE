import string
s = open('10.txt').readline()
alf_full = string.ascii_uppercase
k = set()
print(s)
alf = '0123456789ABCDEFGHI'
for x in s:
    if x not in alf:
        s = s.replace(x, '@')
        k.add(x)
    print(k)
    if 36 - len(k) == 19:
        break
s = s.split('@')
dv = ''
mx = 0
for x in s:
    if x != '' and x[0] != '0' and x[-1] in alf[::2]:
        if int(x, 19) >= mx:
            mx = max(mx, int(x, 19))
for x in s:
    if x != '' and x[0] != '0' and x[-1] in alf[::2]:
        if int(x, 19) == mx:
            print(x)

print(mx)