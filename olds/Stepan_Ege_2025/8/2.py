import itertools
ct = 0
for x in itertools.product('012345678', repeat=6):
    x = ''.join(x)
    if x[0] != '0' and (x.count('1') + x.count('3') + x.count('5') + x.count('7')) <= 2:
        if sum(map(int, str(x))) % 6 == 0 and sum(map(int, str(x))) % 4 != 0:
            ct += 1
print(ct)