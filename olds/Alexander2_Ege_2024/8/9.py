import itertools
ct = 0
for x in itertools.product('012345678', repeat=6):
    x = ''.join(x)
    if x[0] != '0':
        if int(x) % 2 == 0:
            x = x.replace('0', '$')
            x = x.replace('2', '$')
            x = x.replace('4', '$')
            x = x.replace('6', '$')
            x = x.replace('8', '$')
            if x.count('$') <= 2:
                print(x)
                ct +=1
print(ct)