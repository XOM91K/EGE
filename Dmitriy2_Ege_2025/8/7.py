import itertools
ct = 0
for x in itertools.permutations('КОМЕТА', 6):
    x = ''.join(x)
    x = x.replace('К', '*')
    x = x.replace('М', '*')
    x = x.replace('Т', '*')
    x = x.replace('О', '%')
    x = x.replace('Е', '%')
    x = x.replace('А', '%')
    if '**' not in x and '%%' not in x:
        ct += 1
print(ct)