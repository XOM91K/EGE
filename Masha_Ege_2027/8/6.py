import itertools
ct=  0
for x in itertools.permutations('КОМЕТА', 6):
    x = ''.join(x)
    x = x.replace('О', '$')
    x = x.replace('Е', '$')
    x = x.replace('А', '$')
    x = x.replace('К', '%')
    x = x.replace('М', '%')
    x = x.replace('Т', '%')
    if '%%' not in x and '$$' not in x:
        print(x)
        ct += 1
print(ct)