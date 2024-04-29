import itertools
ct = 0
for x in itertools.permutations('ВЕБИНАР', 7):
    x = ''.join(x)
    x = x.replace('А', '1')
    x = x.replace('И', '1')
    x = x.replace('Е', '1')
    x = x.replace('В', '0')
    x = x.replace('Б', '0')
    x = x.replace('Н', '0')
    x = x.replace('Р', '0')
    if '11' not in x and '00' not in x:
        print(x)
        ct += 1
print(ct)





