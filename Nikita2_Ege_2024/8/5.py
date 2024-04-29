import itertools
ct = 0
for x in itertools.product('КОНФЕТА', repeat=5):
    x = ''.join(x)
    x = x.replace('Е', '#')
    x = x.replace('А', '#')
    x = x.replace('О', '#')
    x = x.replace('К', '%')
    x = x.replace('Н', '%')
    x = x.replace('Ф', '%')
    x = x.replace('Т', '%')
    if '##' not in x and x.count('#') >= 2:
        ct += 1
        print(x)
print(ct)