import itertools
ct = 0
for x in itertools.product('КОНФЕТА', repeat=5):
    x = ''.join(x)
    x = x.replace('О', 'А')
    x = x.replace('Е', 'А')
    x = x.replace('К', 'Б')
    x = x.replace('Ф', 'Б')
    x = x.replace('Т', 'Б')
    x = x.replace('Н', 'Б')
    if x.count('А') >= 2 and 'АА' not in x:
        print(x)
        ct += 1
print(ct)