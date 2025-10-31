import itertools
ct = 0
for x in itertools.product('012345678',repeat = 6):
    s = ''.join(x)
    if s[-1] not in '23' and x.count('1') >= 2:
        for c in '01357':
            s = s.replace(c,'*')
        if s[0] != '*':
            ct+=1
print(ct)