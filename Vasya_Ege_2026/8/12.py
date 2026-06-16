import itertools

ct = 0
for x in itertools.product('01234567', repeat=5):
    x = ''.join(x)
    if x[0] not in '01357' and x.count('7') <= 2 and x[-1] not in '62':
        ct += 1
print(ct)