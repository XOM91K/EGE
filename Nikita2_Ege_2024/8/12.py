import itertools
k = 0
c = 0
for x in itertools.product('АВИКПРЧЫ', repeat=5):
    x = ''.join(x)
    k += 1
    if k % 5 != 0:
        c += 1
        if 'А' not in x and 'И' not in x and 'Ы' not in x:
            if len(set(x)) == 5:
                print(c, x)