import itertools
ct=0
for x in itertools.product("ВЕБИНАР",repeat=7):
    x="".join(x)
    if len(set(x)) == 7:
        for y in 'ЕИА':
            x = x.replace(y, '#')
        for y in 'ВБНР':
            x = x.replace(y, '@')
        if '##' not in x and '@@' not in x:
            ct+=1
print(ct)