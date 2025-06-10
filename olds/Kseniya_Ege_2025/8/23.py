import itertools
k = 0
n = 0
for x in itertools.product('АВИКПРЧЫ', repeat=5):
    x = ''.join(x)
    n += 1
    if n % 5 != 0:
        k += 1
        if len(set(x)) == 5:
            x = x.replace('В', 'К')
            x = x.replace('П', 'К')
            x = x.replace('Р', 'К')
            x = x.replace('Ч', 'К')
            if x.count('К') == 5:
                print(k, x)

#ctrl + /