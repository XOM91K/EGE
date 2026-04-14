def dels(d):
    dls=[]
    for x in range(2, int(d**0.5)+1):
        if d % x == 0:
            if str(x)[-2:] == '11' and x != 11:
                dls.append(x)
            if str(d//x)[-2:] == '11' and (d//x) != 11:
                dls.append(d//x)
    return sorted(set(dls))
for x in range(1_350_051, 10 ** 10):
    l = dels(x)
    if len(l)>0:
        print(x, *l)