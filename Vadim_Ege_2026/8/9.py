import itertools
c = 0
sogl = 'ХЛБНЙМКШ'
for x in itertools.permutations("ХЛЕБНЫЙМЯКИШ", 7):
    x = ''.join(x)
    if x[0] == "Х" and x[3] in "БЫКИШ":
        for y in 'ХЛБНЙМКШ':
            x = x.replace(y, '#')
        if '##' not in x:
            c+=1
print(c)