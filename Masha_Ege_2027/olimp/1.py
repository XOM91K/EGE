import itertools
ct = 0
for x in itertools.product('0123456789', repeat=3):
    x = ''.join(x)
    if sum(map(int, x)) % 9 == 0:
        ct += 1
print(ct)