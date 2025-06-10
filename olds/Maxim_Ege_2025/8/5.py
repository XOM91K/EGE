import itertools
k = 0
for x in itertools.product("БНПЭ", repeat=4):
    x = "".join(x)
    k += 1
    if "ЭЭ" not in x and x[0] != "П" and x[-1] != "П" and k %2 == 0:
        print(k,x)