import itertools
k = 0
for x in itertools.product('АБРШ', repeat =5):
    x = ''.join(x)
    k += 1
    if len(set(x)) == 4:
        x = x.replace('Б', '%')
        x = x.replace('Р', '%')
        x = x.replace('Ш', '%')
        if x.count('%') <= 3:
            print(k, x)