import itertools
k = 0
for x in itertools.product("БНПЭ", repeat=4):
    x = ''.join(x)
    k = k + 1
    if x[0] != 'П' and x[3] != 'П' and k % 2 == 0 and 'ЭЭ' not in x :
        print(k, x)