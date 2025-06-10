import itertools
ct = 0
for x in itertools.product('НИКОЛАЙ', repeat=4):
    x = ''.join(x)
    if x[0] != 'Й' and (x.count('И') + x.count('О') + x.count('А')) >= 1:
        ct += 1
print(ct)