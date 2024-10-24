import itertools
k = 0
for x in set(itertools.product('СВЯТОСЛАВ', repeat = 7)):
    x = ''.join(x)
    if (x.count('Я')+x.count('О')+x.count('А')) > (x.count('С')+x.count('В')+x.count('Т')+x.count('Л')):
        k = k+1
print(k)