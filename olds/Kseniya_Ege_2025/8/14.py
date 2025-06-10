import itertools
ct = 0
for x in set(itertools.product('СВЯТОСЛАВ', repeat=7)):
    x = ''.join(x)
    x = x.replace('О', 'Я')
    x = x.replace('А', 'Я')
    x = x.replace('В', 'С')
    x = x.replace('Т', 'С')
    x = x.replace('Л', 'С')
    if x.count('Я') > x.count('С'):
        ct += 1
print(ct)