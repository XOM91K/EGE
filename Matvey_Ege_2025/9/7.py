l = [sorted([int(d) for d in x.split()]) for x in open('7.txt')]
k = 0
for x in l:
    ch = 0
    nch = 0
    kk = 0
    if len(set(x)) == 4:
        kk += 1
    for i in range(5):
        if x[i] % 2 == 0:
            ch += x[i]
        else:
            nch += x[i]
    if nch > ch:
        kk += 1
    if kk == 1:
        k += 1
print(k)