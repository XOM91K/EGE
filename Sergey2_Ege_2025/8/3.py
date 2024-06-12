import itertools
k = 0
for x in itertools.product('ГЕНОСТХЮ', repeat=4):
    x = ''.join(x)
    k += 1
    if k % 2 == 1 and x[0] != 'Н' and x.count('О') >= 2 and x.count('С') == 0:
        print(k, x)