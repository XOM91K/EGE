import itertools
ct = 0
for x in itertools.permutations('ВЕБИНАР', 7):
    x = ''.join(x)
    x = x.replace('В', '#')
    x = x.replace('Б', '#')
    x = x.replace('Н', '#')
    x = x.replace('Р', '#')
    x = x.replace('И', '@')
    x = x.replace('Е', '@')
    x = x.replace('А', '@')
    if '##' not in x and '@@' not in x:
        ct += 1
print(ct)