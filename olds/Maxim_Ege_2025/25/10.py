def dels(d):
    dls = []
    for x in range(1,int(d**0.5)+1):
        if d%x == 0:
            dls.append(x)
            dls.append(d//x)
    dls = sorted(set(dls))
    dls = dls[1:-1]
    if len(dls) == 0:
        M = 0
    else:
        M = sum(dls)/len(dls)
    return int(M)
for y in range(700000,650000,-1):
    if str(dels(y))[-3:] == '313':
        print(y,dels(y))