import itertools
k=0
for x in itertools.product("ГАЛКТИ", repeat=8):
    x="".join(x)
    if x[0] in "ГЛКТ" and (x[-1] in 'АИ') and "КЛ" not in x:
        k+=1
        print(k)