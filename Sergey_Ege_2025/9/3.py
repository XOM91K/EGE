l = [[int(d) for d in x.split()] for x in open('3.txt')]
ct = 0
for x in l:
    ch = 0
    nch = 0
    usl = 0
    if len(set(x)) == 4:
        usl += 1
    for y in x:
        if y % 2 == 0:
            ch += y
        else:
            nch += y
    if nch > ch:
        usl += 1
    if usl == 1:
        ct += 1
print(ct)
