ct = 0
import itertools
for x in itertools.product('012345678', repeat=6):
    x = ''.join(x)
    if x[0] != '0':
        if int(x, 9) % 2 == 0:
            if x.count('0') + x.count('2') + x.count('4') + x.count('6') + x.count('8') <= 2:
                ct += 1
print(ct)