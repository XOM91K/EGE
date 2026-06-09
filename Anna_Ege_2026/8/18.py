import itertools

ct = 0
for x in itertools.product('1234567890abcd', repeat=5):
    x = ''.join(x)
    if x[0] != '0':
        flag = False
        ct_nch = 0
        for z in '13579bd':
            ct_nch += x.count(z)
            if x.count(z) == 2:
                flag = True
        for z in '13579bd':
            x = x.replace(z, '#')
        for z in '02468ac':
            x = x.replace(z, '@')
        if '#@#' in x and flag == True and ct_nch == 2:
            ct += 1
            print(x)
print(ct)

