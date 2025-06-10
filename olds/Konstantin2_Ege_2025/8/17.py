import itertools
ct = 0
for x in itertools.product('012345678', repeat = 5):
    x = ''.join(x)
    if x.count('0') == 1 and x[0] != '0':
        if '03' not in x and '30' not in x and '01' not in x and '10' not in x and\
                '05' not in x and '50' not in x and '07' not in x and '70' not in x:
            print(x)
            ct += 1
print(ct)