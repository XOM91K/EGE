l = [sorted([int(d) for d in x.split()]) for x in open('7.txt')]
ct = 0
for x in l:
    ch = 0
    nch = 0
    for y in x:
        if y % 2 == 0:
            ch += y
        else:
            nch += y
    k = 0
    if len(set(x)) == 4:
        k += 1
    if nch > ch:
        k += 1
    if k == 1:
        ct += 1
print(ct)