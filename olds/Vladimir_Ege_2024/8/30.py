import itertools
k = 0
for x in itertools.product('0123456789', repeat = 5):
    x = ''.join(x)
    if x[0] != '0' and x.count('2') == 1:
        if '02' not in x and '20' not in x and '42' not in x and '24' not in x and '62' not in x and '26' not in x and '82' not in x and '28' not in x:
            k += 1
print(k)