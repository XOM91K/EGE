def dels(d):
    l = []
    for x in range(2, int(d ** 0.5)+1):
        if d % x == 0:
            if str(x)[-2:] =='11' and x != 11:
                l.append(x)
            if str(d//x)[-2:] == '11' and (d//x) != 11:
                l.append(d//x)
    return sorted(set(l))

for x in range(1_350_051, 5_000_000):
    m = dels(x)
    if len(m)>0:
        print(x, min(m))