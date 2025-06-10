import itertools
ct = 0
for x in itertools.permutations('ВЕБИНАР', 7):
    x = ''.join(x)
    x = x.replace('В', '@')
    x = x.replace('Б', '@')
    x = x.replace('Н', '@')
    x = x.replace('Р', '@')
    if x.count('@@') == 0 and x.count('11') == 0:
        ct += 1
print(ct)