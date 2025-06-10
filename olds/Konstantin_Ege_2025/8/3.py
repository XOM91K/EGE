import itertools
k = 0
for x in itertools.product('ГЕНОСТХЮ', repeat=4):
    x = ''.join(x)
    k += 1
    if k % 2 != 0:
        if x[0] != 'Н' and 'С' not in x and x.count('О') >= 2:
            print(k, x)