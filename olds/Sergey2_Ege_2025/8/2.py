import itertools
k = 0
for x in itertools.product('ВЕЖКЛРШ', repeat=6):
    x = ''.join(x)
    k +=1
    if x[0] == 'К' and x[5] == 'Ш':
        print(k, x)