import itertools
ct = 0
for x in itertools.product("567", repeat = 12):
    x = ''.join(x)
    if "55" not in x:
        ct+=1
print(ct)