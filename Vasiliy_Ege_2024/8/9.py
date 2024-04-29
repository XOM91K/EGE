import itertools
ct = 0
for x in itertools.product('012345678', repeat=7):
    x = ''.join(x)
    # 0128414
    if x[0] not in '0246':
        if "000"not in x[-3:] and "111" not in x[4:] and "222" not in x[4:7] and "333" not in x[4:7] and "444" not in x[4:7] and "555" not in x[4:7] and "666" not in x[4:7] and "777" not in x[4:7] and "888" not in x[4:7]:
            ct += 1
print(ct)