import itertools
ct = 0
for x in itertools.product('ТИМОФЕЙ', repeat=6):
    x = ''.join(x)
    if x.count('И') + x.count('Е') + x.count('О') == x.count('Й') \
                    + x.count('Т') + x.count('М') + x.count('Ф'):
        ct += 1
print(ct)