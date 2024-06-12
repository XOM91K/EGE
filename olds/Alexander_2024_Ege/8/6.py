import itertools
ct = 0
for x in itertools.product('ТИМОФЕЙ', repeat=6):
    x = ''.join(x)
    if (x.count('Т') + x.count('М') + x.count('Ф') + x.count('Й')) == (x.count('И') + x.count('О') + x.count('Е')):
        ct += 1
print(ct)