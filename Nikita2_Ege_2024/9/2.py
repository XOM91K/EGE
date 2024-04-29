l = [[int(d) for d in x.split()] for x in open('2.txt')]
ct = 0
for x in l:
    k = 0
    smnch = 0
    smch = 0
    for y in x:
        if y % 2 == 0:
            smch += y
        else:
            smnch += y
    if smnch > smch:
        k += 1
    if len(set(x)) == 4:
        k += 1
    if k == 1:
        ct += 1
print(ct)