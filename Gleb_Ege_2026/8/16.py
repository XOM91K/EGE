import itertools
ct = 0
for x in itertools.product('0123456789abcd', repeat=5):
    x = ''.join(x)
    if x[0] != '0':
        flag = 'NO'
        ct_nech = 0
        for y in '0123456789abcd'[1::2]:
            ct_nech += x.count(y)
            if x.count(y) == 2:
                flag = 'YES'
        if ct_nech == 2 and flag:
            for y in '0123456789abcd'[1::2]:
                x = x.replace(y, '#')
            for y in '0123456789abcd'[0::2]:
                x = x.replace(y, '@')
            if '#@#' in x:
                ct += 1
print(ct)