import itertools
ct = 0
for x in itertools.product('01234567', repeat = 5):
    x = ''.join(x)
    if x[0] == '7' and (('65' in x and '56' not in x) or ('56' in x and '65' not in x)) and int(x[-1]) % 2 == 0:
            print(x)
            ct += 1
print(ct)