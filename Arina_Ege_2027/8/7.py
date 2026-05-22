import itertools
ct = 0
for x in itertools.product("АРСТЫ", repeat=5):
    x = ''.join(x)
    ct+=1
    if x[0] == "С":
        if len(set(x)) == 5:
            print(ct, x)