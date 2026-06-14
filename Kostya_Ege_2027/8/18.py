import itertools, string
print(string.ascii_uppercase)
ct = 0
for x in itertools.product('0123456789ABCDEFGHIJKLMNO', repeat=4):
    x = ''.join(x)
    if x[0] != '0':
        ct_chet = [d for d in x if d in '0123456789ABCDEFGHIJKLMNO'[::2]]
        if len(ct_chet) >= 1:
            ct_cif15 = [d for d in x if d in 'GHIJKLMNO']
            if len(ct_cif15) > 2:
                ct += 1
print(ct)