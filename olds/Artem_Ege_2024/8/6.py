import itertools
ct = 0
for x in itertools.product('ТИМОФЕЙ', repeat=6):
    x = ''.join(x)
    x = x.replace('Т', '0')
    x = x.replace('М', '0')
    x = x.replace('Ф', '0')
    x = x.replace('Й', '0')
    x = x.replace('И', '1')
    x = x.replace('О', '1')
    x = x.replace('Е', '1')
    if x.count('0') == x.count('1'):
        print(x)
        ct += 1
print(ct)