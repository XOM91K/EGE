import itertools
c = 0
for i in itertools.product("0123456", repeat=6):
    e = ''
    for j in i:
        e += j
    e = int(e)
    e = str(e)
    print(e)
    if e.count("0") == 1:
        k = 0
        for j in i:
            if int(j) % 2 == 0 and j != "0":
                k += 1
        if k % 2 == 0:
            c += 1
print(c)