import itertools
ct = 0
for x in itertools.product('ТИМОФЕЙ', repeat=6):
    x = ''.join(x)
    if x.count('И') + x.count('О') + x.count('Е') == 3:
        print(x)
        ct += 1
print(ct)