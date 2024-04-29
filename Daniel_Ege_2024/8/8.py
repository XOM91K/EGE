from itertools import product
ct = 0
for x in product('01234567', repeat=5):
    x = ''.join(x)
    if x[0] != '0' and x[0] not in '1357' and x[-1] not in '26' and x.count('7') <= 2:
        ct += 1
        print(x)
print(ct)