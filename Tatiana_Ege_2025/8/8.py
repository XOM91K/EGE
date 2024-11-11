import itertools
ct = 0
for x in itertools.product('123456789abcde', repeat=6):
    x = ''.join(x)
    if x.count('a') + x.count('b') + x.count('c') + x.count('d') + x.count('e') <= 4:
        ct += 1
print(ct)
#7!/ 2!(7-2)!
#6 * 7 / 2