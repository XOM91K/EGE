import itertools
ct = 0
k = 0
mas = []
for x in itertools.product(sorted('ЕКУРСИЯ'), repeat=6):
    x = ''.join(x)
    ct+=1
    if ct % 2 == 0:
        if x[0] != 'К':
            x = x.replace('Е', '$')
            x = x.replace('У', '$')
            x = x.replace('И', '$')
            x = x.replace('Я', '$')
            if x.count('$') <= 2:
                k += 1
print(k)