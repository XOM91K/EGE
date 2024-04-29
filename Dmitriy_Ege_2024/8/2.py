import itertools
ct = 0
for x in set(itertools.product('ГАЛАКТИКА', repeat=8)):
    #согл: Г Л К Т
    # гл: А И
    x = ''.join(x)
    if x[0] in 'ГЛКТ' and x[-1] in 'АИ':
        if (ord(x[1]) - ord(x[0]) != 1) and (ord(x[2]) - ord(x[1]) != 1) and (ord(x[3]) - ord(x[2]) != 1) and (ord(x[4]) - ord(x[3]) != 1) and (ord(x[5]) - ord(x[4]) != 1) and (ord(x[6]) - ord(x[5]) != 1) and (ord(x[7]) - ord(x[6]) != 1):
            ct += 1
print(ct)