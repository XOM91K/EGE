from itertools import permutations
ct = 0
for x in permutations('ЯРОСЛАВ', 5):
    x = ''.join(x)
    x = x.replace('Я', 'А')
    x = x.replace('О', 'А')
    x = x.replace('С', 'Р')
    x = x.replace('Л', 'Р')
    x = x.replace('В', 'Р')
    if x.count('Р') > x.count('А'):
        if 'АА' not in x:
            ct += 1
print(ct)