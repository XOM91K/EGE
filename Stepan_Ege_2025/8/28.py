import itertools
ct = 0
for x in itertools.product('ДГИАШЭ', repeat = 5):
    x = ''.join(x)
    x = x.replace('А', '@')
    x = x.replace('И', '@')
    x = x.replace('Э', '@')
    x = x.replace('Д', '№')
    x = x.replace('Г', '№')
    x = x.replace('Ш', '№')
    if x[0] != '@' and x[-1] != '№':
        ct += 1
        print(ct, x)