import itertools
ct = 0
for x in itertools.product('255', repeat=6):
    x = ''.join(x)
    if x[0] != '0':
        if x.count('2') == 1:
            if '20' in x:
                ct += 1
print(ct)