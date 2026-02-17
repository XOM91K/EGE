import itertools
k = 0
for x in itertools.product('ГЕКЭ023', repeat=4):
    x = ''.join(x)
    k += 1
    #if x[0] in '023':
    if x[0] == '0' or x[0] == '2' or x[0] == '3':
        if 'КК' not in x and 'ЕЕ' not in x and 'ЭЭ' not in x and 'ГГ' not in x and '00' not in x and '22' not in x and '33' not in x:
            print(k, x)
