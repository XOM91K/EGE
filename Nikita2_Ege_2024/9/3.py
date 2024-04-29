l = [sorted([int(d) for d in x.split()]) for x in open('3.txt')]
ct = 0
for x in l:
    sm_ch = 0
    sm_nch = 0
    k = 0
    if len(set(x)) == 4:
        k += 1
    for y in x:
        if y % 2 == 0:
            sm_ch += y
        else:
            sm_nch += y
    if sm_nch > sm_ch:
        k += 1
    if k == 1:
        ct += 1
print(ct)