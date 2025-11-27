import itertools
ct = 0
for x in itertools.product('0123456789AB', repeat=5):
    x = ''.join(x)
    if x.count('7') == 1 and x[0] != '0':
        for l in '9AB' :
            x = x.replace(l,'*')
        if x.count('*') <= 3 :
            ct += 1
print(ct)