import itertools, string
ct = 0
alf = '0123456789abcdefghijklmno'
for x in itertools.product('0123456789abcdefghijklmno', repeat = 4):
    x = ''.join(x)
    if x[0] != '0':
        sm_cif = 0
        for y in x:
            sm_cif += alf.index(y)
        if sm_cif % 5 == 0:
            for y in '02468acegikmo':
                x = x.replace(y, '@')
            for p in '13579bdfhjln':
                x = x.replace(p, '#')
            if x.count('@@') + x.count('##') == 0:
                    ct += 1
                    print(ct)
print(string.ascii_uppercase)