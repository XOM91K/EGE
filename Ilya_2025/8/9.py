import itertools
ct = 0
for x in itertools.product('0123456789abcdef', repeat=6):
    x = ''.join(x)
    if x[0] not in '01' and x[4:] == 'ab':
        ct += 1
        print(x)
print(ct)