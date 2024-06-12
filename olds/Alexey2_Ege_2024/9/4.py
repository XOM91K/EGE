l = [[int(d) for d in x.split()] for x in open('4.txt')]

obshiy_ct = 0
for x in l:
    ct = 0
    nechet = 0
    for y in x:
        if y % 2 != 0:
            nechet += 1
    if nechet == 3:
        ct += 1
    if len(set(x)) < 6:
        ct += 1
    if ct == 1:
        obshiy_ct += 1


print(obshiy_ct)