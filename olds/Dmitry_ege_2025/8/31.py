import itertools, string
print(string.ascii_uppercase)
alf = '0123456789ABCDEFGHIJKLMNO'
ct = 0
for x in itertools.product('0123456789ABCDEFGHIJKLMNO', repeat=4):
    x = ''.join(x)
    if (alf.index(x[0]) + alf.index(x[1]) + alf.index(x[2]) + alf.index(x[3])) % 5 == 0:
        if alf.index(x[0]) % 2 != alf.index(x[1]) % 2 and alf.index(x[1]) % 2 != alf.index(x[2]) % 2 and alf.index(x[2]) % 2 != alf.index(x[3]) % 2:
            if x[0] != '0':
                ct += 1
print(ct)