import itertools
ct = 0
for x in set(itertools.product('СВЯТОСЛАВ', repeat=7)):
    x = ''.join(x)
    gl = x.count('А') + x.count('О') + x.count('Я')
    sg = x.count('С') + x.count('В') + x.count('Т') + x.count('Л')
    if gl > sg:
        ct += 1
        print(x)
print(ct)