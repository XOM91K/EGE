ct = 0
import itertools
for x in itertools.product('123456789abcdef', repeat=6):
    x = ''.join(x)
    ctb = 0
    for y in 'abcdef':
        ctb += x.count(y)
    if ctb <= 4:
        ct += 1
print(ct * 21)
#229405365