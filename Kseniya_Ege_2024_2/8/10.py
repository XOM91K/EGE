import itertools
ct = 0
for x in itertools.product("БАНДЕРОЛЬ", repeat=7):
    x = ''.join(x)
    if x.count('Ь') <= 1:
        x = x.replace('Б', '2')
        x = x.replace('Н', '2')
        x = x.replace('Д', '2')
        x = x.replace('Р', '2')
        x = x.replace('Л', '2')
        if '2Е' not in x and 'Е2' not in x:
            ct +=1
print(ct)