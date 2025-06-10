import itertools
nm = 0
ct = 0
for x in itertools.product('БЖОУФЦЮ', repeat=4):
    x = ''.join(x)
    nm += 1
    if x[0:2] == 'ЖО' and nm % 2 == 0:
        ct += 1
print(ct)