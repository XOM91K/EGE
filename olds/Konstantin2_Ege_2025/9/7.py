l = [sorted([int(d) for d in x.split()]) for x in open('7.txt')]
ct = 0
for x in l:
    k = 0
    if len(set(x)) == 4:
        k += 1
    ch = 0
    nch = 0
    for y in range(len(x)):
        if x[y] % 2 == 0:
            ch += x[y]
        else:
            nch += x[y]
    if nch > ch:
        k += 1
    if k == 1:
        ct += 1
print(ct)