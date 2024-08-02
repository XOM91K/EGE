import itertools
k = 0
for x in itertools.product('АГМНСТУ', repeat=6):
    x = ''.join(x)
    k += 1
    if x[0] != 'У' and x.count('М') == 2 and x.count('Г') <= 1:
        print(k, x)