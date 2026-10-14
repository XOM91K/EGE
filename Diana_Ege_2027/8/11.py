import itertools
ct=0
for x in itertools.product("НИКОЛАЙ", repeat=4):
    x=''.join(x)
    if x[0] !='Й':
        if x.count('И')+ x.count('А') + x.count('О') >= 1:
            ct+=1
print(ct)