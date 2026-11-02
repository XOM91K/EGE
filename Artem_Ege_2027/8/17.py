import itertools
k = 0
for x in itertools.product(('ГЕКЭ023'), repeat = 4 ):
    x = ''.join(x)
    k += 1
    x = x.replace('0' , '#')
    x = x.replace('2', '#')
    x = x.replace('3', '#')
    if x[0] == '#':
        if 'КК' not in x:
            if 'ЕЕ' not in x:
                if 'ГГ' not in x:
                    if 'ЭЭ' not in x:
                        if '##' not in x:
                            print(k)