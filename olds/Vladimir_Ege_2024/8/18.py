import itertools
ct = 0
for x in itertools.product('0123456', repeat=6):
    x = ''.join(x)
    if x[0] != '0' and x.count('3') == 1 and '13' not in x and '31' not in x and '11' not in x and '35' not in x and '53' not in x and '51' not in x and '15' not in x and '55' not in x:
        ct += 1
print(ct)