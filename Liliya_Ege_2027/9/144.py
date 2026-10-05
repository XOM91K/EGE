l = [[int(d) for d in x.split()] for x in open('144.txt')]
ct = 0
for x in l:
    ch = sum([d for d in x if d % 2 == 0])
    nch = sum([d for d in x if d % 2 != 0])
    k = 0
    if len(set(x)) == 4:
        k += 1
    if nch > ch:
        k += 1
    if k == 1:
        ct += 1
print(ct)