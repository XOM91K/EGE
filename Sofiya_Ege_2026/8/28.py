import itertools
ct=0
d=[]
for x in itertools.product('0123456789ABCD',repeat=5):
    x=''.join(x)
    if x[0]!='0':
        flag = 'NO'
        for y in '0123456789ABCD'[1::2]:
            if x.count(y) == 2:
                flag = 'YES'
            x = x.replace(y, '#')
        for y in '0123456789ABCD'[::2]:
            x = x.replace(y, '@')
        if x.count('#') == 2 and flag and '#@#' in x:
            ct+=1
            print(x)
            d.append(x)
print(ct)