import itertools
cnt = 0
for x in itertools.product("0123456789ABC", repeat=6):
    x = "".join(x)
    if x.count("2")==1 and x[0] != '0':
        if x.count('A') + x.count('B') + x.count('C') <= 4:
            cnt += 1
print(cnt)