import itertools
ct = 0
for x in itertools.product('АПРСУ', repeat=4):
    x = ''.join(x)
    ct += 1
    if 'А' not in x:
        print(x, ct)
        break
