import itertools
k2 = 0
for x in itertools.product('01234567', repeat=5):
    x = ''.join(x)
    if x[0] != '0' and x.count('3') <= 1:
        x = x.replace('3', '1')
        x = x.replace('5', '1')
        x = x.replace('7', '1')
        if '11' not in x:
            k2 += 1
            print(x)
print(k2)