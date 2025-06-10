import itertools
ct=0
for x in set(itertools.product('СВЯТОСЛАВ', repeat=7)):
    x=''.join(x)
    if x.count('Я') + x.count('А') + x.count('О') > x.count('Т') + x.count('С') + x.count('В') +  x.count('Л'):
        ct+=1
print(ct)
s = 'abracadabra'
print(len(set(s)))