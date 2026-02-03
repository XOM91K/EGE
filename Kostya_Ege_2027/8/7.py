import itertools
ct = 0
for x in itertools.product("01234567", repeat=5):
    x = "".join(x)
    if x[0] != '0':
        if x.count("7") <= 2:
            if x[0] in '246' and x[-1] not in '26':
                ct += 1
print(ct)