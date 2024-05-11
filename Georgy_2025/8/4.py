import itertools

k = 0
for x in itertools.product("БНПЭ", repeat=4):
    x = "".join(x)
    k += 1
    if k % 2 == 0 and x[0] != "П" and x[-1] != "П" and 'ЭЭ' not in x:
        print(k, x)
