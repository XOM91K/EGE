import itertools
ct = 0
for x in set(itertools.product('СВЯТОСЛАВ', repeat = 7)):
    x = ''.join(x)
    x = x.replace('Я', '@')
    x = x.replace('О', '@')
    x = x.replace('А', '@')
    x = x.replace('С', '#')
    x = x.replace('В', '#')
    x = x.replace('Т', '#')
    x = x.replace('С', '#')
    x = x.replace('Л', '#')
    x = x.replace('В', '#')
    if x.count('@') > x.count('#'):
        ct += 1
print(ct)