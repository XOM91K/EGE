import itertools
ct = 0
for x in itertools.product('012345678', repeat=6):
    x = ''.join(x)
    ct_nech = x.count('1') + x.count('3') + x.count('5') + x.count('7')
    if ct_nech < 3 and x[0] != '0':
        if sum(list(map(int, x))) % 6 == 0 and sum(list(map(int, x))) % 4 != 0:
            ct += 1
            print(x)
print(ct)