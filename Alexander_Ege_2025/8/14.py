import itertools

cnt = 0
for x in itertools.product("0123456789AB", repeat=5):
    x = "".join(x)
    if x.count('7') == 1 and x[0] != "0":
        if x.count('9') + x.count('A') + x.count('B') <= 3:
            cnt += 1
print(cnt)