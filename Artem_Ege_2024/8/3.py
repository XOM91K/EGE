import itertools
ct = 0
for x in itertools.product('АГМНСТУ', repeat=6):
    x = ''.join(x)
    ct += 1
    if x[0] != 'У' and x.count('М') == 2 and x.count('Г') <= 1:
        print(x, ct)
print(ct)