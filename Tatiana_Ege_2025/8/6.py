import itertools
c = 0
for i in set(itertools.product("СВЯТОСЛАВ", repeat=7)):
    i = ''.join(i)
    g = 0
    for j in i:
        if j in "ЯОА":
            g += 1
    if g > len(i) - g:
        c += 1
print(c)
