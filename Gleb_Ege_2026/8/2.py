import itertools
ct = 0
for x in itertools.product('БРОНХИ', repeat=4):
    x = ''.join(x)
    if x.count('Х') == 1:
        ct += 1
print(ct)