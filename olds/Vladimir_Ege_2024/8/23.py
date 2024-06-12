import itertools
ct = 0
for x in itertools.permutations('ХОЧУНАБЮДЖЕТ'):
    x = ''.join(x)
    x = x.replace('О', '#')
    x = x.replace('У', '#')
    x = x.replace('А', '#')
    x = x.replace('Ю', '#')
    x = x.replace('Е', '#')
    if '#####' not in x:
        ct += 1
print(ct)