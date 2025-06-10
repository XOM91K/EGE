l = [sorted([int(d) for d in x.split()]) for x in open('13.txt')]
ct = 0
for x in l:
    cht = []
    ne_cht = []
    for y in x:
        if y % 2 == 0:
            cht.append(y)
        else:
            ne_cht.append(y)
    if len(cht) > 0 and len(ne_cht) > 0:
        if len(cht) % 2 == 0 and len(ne_cht) % 2 != 0:
            if max(cht) % 4 == 0:
                ct +=1
print(ct)