import itertools
ct=0
for x in itertools.product('0123456789ABCDEF',repeat=5):
    x=''.join(x)
    # 23444
    can = True
    for y in '0123456789ABCDEF':
        if x.count(y) > 2:
            can = False
    if can:
        if ('1' in x or '4' in x or '9' in x) and x[0] != '0':
            ct += 1
print(ct)