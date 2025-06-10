import itertools
k = 0
for x in set(itertools.product('СВЯТОСЛАВ', repeat=7)):
    x = ''.join(x)
    x = x.replace('С', '0')
    x = x.replace('В', '0')
    x = x.replace('Я', '1')
    x = x.replace('Т', '0')
    x = x.replace('О', '1')
    x = x.replace('Л', '0')
    x = x.replace('А', '1')
    if x.count('1') > x.count('0'):
        k += 1
print(k)